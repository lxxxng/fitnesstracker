# Barbell Exercise Classification and Rep Counting with Accelerometer and Gyroscope Data

## Project Overview
This project processes accelerometer and gyroscope data from the MetaMotion sensor to classify barbell exercises and count repetitions. It involves cleaning the data, visualizing it, performing feature engineering, building machine learning models, and developing a custom algorithm to count repetitions.

---

## Tutorial Reference
This project follows the tutorial available on YouTube: [Barbell Exercise Classification and Rep Counting Tutorial](https://www.youtube.com/watch?v=cCONIdrM2VI&list=PL-Y17yukoyy0sT2hoSQxn1TdV0J7-MX4K)
It is one of the best tutorials with clear explanations and minimal bugs that can be easily fixed. 

---

## Table of Contents
1. [Introduction, Goal, and Dataset](#introduction-goal-and-dataset)
2. [Converting Raw Data, Reading CSV Files, Splitting Data, Cleaning](#converting-raw-data-reading-csv-files-splitting-data-cleaning)
3. [Visualizing Data, Plotting Time Series Data](#visualizing-data-plotting-time-series-data)
4. [Outlier Detection, Chauvenet’s Criterion, Local Outlier Factor](#outlier-detection-chauvets-criterion-local-outlier-factor)
5. [Feature Engineering, Frequency, Low Pass Filter, PCA, Clustering](#feature-engineering-frequency-low-pass-filter-pca-clustering)
6. [Predictive Modelling, Naive Bayes, SVMs, Random Forest, Neural Network](#predictive-modelling-naive-bayes-svms-random-forest-neural-network)
7. [Counting Repetitions, Creating a Custom Algorithm](#counting-repetitions-creating-a-custom-algorithm)

---

## Part 1 — Introduction, Goal, and Dataset
- Understand the problem of exercise classification and rep counting.
- Introduce the MetaMotion sensor and its role in capturing accelerometer and gyroscope data.
- Overview of the dataset containing sensor readings during different barbell exercises.

---

## Part 2 — Converting Raw Data, Reading CSV Files, Splitting Data, Cleaning
- Load the CSV data containing accelerometer and gyroscope sensor readings.
- Clean the data by removing or imputing missing values.
- Split the dataset into training and testing sets for model validation.

---

## Part 3 — Visualizing Data, Plotting Time Series Data
- Visualize accelerometer and gyroscope data using time-series plots.
- Plot sensor data for different exercises to identify patterns and distinguish between them.

---

## Part 4 — Outlier Detection, Chauvenet’s Criterion, Local Outlier Factor
- Apply **Chauvenet’s criterion** to remove extreme outliers from the dataset.
- Use the **Local Outlier Factor (LOF)** algorithm to identify and filter outliers in the data.

---

## Part 5 — Feature Engineering, Frequency, Low Pass Filter, PCA, Clustering
- Extract useful features from the raw sensor data for classification.
- Perform **Fourier Transform** to analyze the frequency components of the sensor data.
- Apply a **Low Pass Filter** to remove high-frequency noise from the sensor signals.
- Use **Principal Component Analysis (PCA)** to reduce the dimensionality of the data.
- Apply **clustering techniques** to identify patterns and group similar movements.

---

## Part 6 — Predictive Modelling, Naive Bayes, SVMs, Random Forest, Neural Network
- Build machine learning models to classify exercises based on accelerometer and gyroscope data.
- Train and evaluate models such as **Naive Bayes**, **Support Vector Machines (SVMs)**, **Random Forest**, and **Neural Networks**.
- Compare model performance to choose the best classifier for the task.

---

## Part 7 — Counting Repetitions, Creating a Custom Algorithm
- Develop a custom algorithm to detect and count repetitions during barbell exercises.
- Implement logic to detect when a repetition starts and ends based on sensor data patterns.
- Fine-tune the algorithm for accuracy in real-time applications.

---
