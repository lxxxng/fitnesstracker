# Example DataFrame and usage
df_temporal = df_squared.copy()  
NumbAbs = NumericalAbstraction()

predictor_columns = predictor_columns + ["acc_r", "gyr_r"] 

ws = int(1000 / 200)  # Window size

# Apply rolling transformations to the entire dataset
for col in predictor_columns:
    df_temporal = NumbAbs.abstract_numerical(df_temporal, [col], ws, "mean")
    df_temporal = NumbAbs.abstract_numerical(df_temporal, [col], ws, "std")

# Process by sets
df_temporal_list = []
for s in df_temporal["set"].unique():
    subset = df_temporal[df_temporal["set"] == s].copy()
    
    # Apply rolling transformations for each column in the subset
    for col in predictor_columns:
        subset.shape()
        subset = NumbAbs.abstract_numerical(subset, [col], ws, "mean")
        subset = NumbAbs.abstract_numerical(subset, [col], ws, "std")
    
    df_temporal_list.append(subset)

# Concatenate all subsets
df_temporal = pd.concat(df_temporal_list, ignore_index=True)