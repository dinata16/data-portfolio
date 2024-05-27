# Credit Card Fraud Detection 💳
<div align="center">
  <img src="https://github.com/dinata16/data-science-projects/assets/89764786/17476a6a-54d2-431e-9021-6305176495ab" alt="creditcard">
</div>

## Project Overview 
This project aims to develop a machine learning model capable of detecting suspicious or potentially fraudulent credit card transactions. This model can help financial institutions to reduce fraud losses and improve customer transaction security.

## About The Dataset
The project utilizes Credit Card Fraud datasets from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data) containing information such as transaction time, transaction amount, and various anonymized features generated through Principal Component Analysis (PCA). This dataset is highly imbalanced, with fraudulent transactions representing only a small fraction of the total transactions.

## Methodology
Exploratory Data Analysis (EDA): Understand the data distribution, identify outliers, and analyze relationships between features.
Data Preprocessing: Handle missing values, perform feature scaling, and address class imbalance (e.g., using oversampling or undersampling techniques).
Feature Selection: Identify the most relevant features for modeling using techniques such as correlation analysis, Recursive Feature Elimination (RFE), or SelectFromModel.
Modeling: Develop machine learning model Random Forest
Model Evaluation: Evaluate model performance using metrics like precision, recall, F1-score, and Area Under the Receiver Operating Characteristic Curve (AUROC).
Hyperparameter Tuning: Optimize model hyperparameters to improve performance.
Results
The best-performing model achieved high accuracy and recall rates in detecting fraudulent transactions. The model is also effective in reducing false positives, which are legitimate transactions incorrectly identified as fraudulent.

## Conclusion
This project demonstrates the potential of machine learning in credit card fraud detection. The developed model can be a valuable tool for financial institutions to enhance transaction security and protect customers from financial losses.

## Suggestions for Further Development
Experiment with more complex model architectures, such as deep learning.
Collect more data to improve model performance.
Develop a real-time system for immediate fraud detection.

## How to Use
Clone this repository.
Install the required dependencies.
Run the provided Jupyter notebook to view the data analysis, modeling, and evaluation.

## Contributions
Contributions are welcome! Please submit a pull request if you have any suggestions or improvements.
