# Telco Customer Churn
  ![Telco](https://github.com/dinata16/data-science-projects/assets/89764786/72bc5235-e9db-497c-b6ec-b43ecbc511b5)


## Project overview
The aim of this project is to analyze customer demographics, area code, states, and other features to predict customer will churn or not. Customer churn defined as when customer discontinue doing bussines with a service or company.

However, if the company could forecast which customer are likely discontinue subscription, it could be focus customer retention only on these 'high risk' customers. So, customer churn is critical metric because it's less expensive to retain existing customers than it's to acquire new customers. 



## About the dataset
The dataset used in this project is sourced from [Kaggle](https://www.kaggle.com/c/customer-churn-prediction-2020/overview) with the training dataset contains 4250 samples an each sample contains 19 features and 1 boolean variable "churn" which indicates the class of the sample. The test dataset have unseen class churn.

Here is a description of features that used to this project

| Features         | Type Data | Description                                                |
|------------------|-----------|------------------------------------------------------------|
| state         | string | 2-letter code of the US state of customer residence |
| account_length | numerical. | Number of months the customer has been with the current telco provider |
|  area_code | string | "area_code_AAA" where AAA = 3 digit area code. |
|  international_plan | (yes/no). |  The customer has international plan. |
|  voice_mail_plan | (yes/no). |  The customer has voice mail plan. |
|  number_vmail_messages | numerical |  Number of voice-mail messages. |
|  total_day_minutes | numerical |  Total minutes of day calls. |
|  total_day_calls | numerical |  Total number of day calls. |
|  total_day_charge | numerical |  Total charge of day calls. |
|  total_eve_minutes | numerical |  Total minutes of evening calls. |
|  total_eve_calls | numerical |  Total number of evening calls. |
|  total_eve_charge | numerical |  Total charge of evening calls. |
|  total_night_minutes | numerical |  Total minutes of night calls. |
|  total_night_calls | numerical |  Total number of night calls. |
|  total_night_charge | numerical |  Total charge of night calls. |
|  total_intl_minutes | numerical |  Total minutes of international calls. |
|  total_intl_calls | numerical |  Total number of international calls. |
|  total_intl_charge | numerical |  Total charge of international calls |
|  number_customer_service_calls | numerical |  Number of calls to customer service |
|  number_customer_service_calls | numerical |  Number of calls to customer service |
|  churn | (yes/no) | Customer churn - target variable. |




## Conclusion
From Exploratory Data Analysis of Final data test, we know that area code 415 has the highest customer will churn of 51. The states have the highest customer churn are TX (Texas) and NC (North Carolina) i.e. 6 and 5. 

Total day charge and total day minutes have an straight relationship churn count where total day charge and total day minutes increase then customer churn will increase too. It can be seen on correlation feaures and data visualization.

Customer use international plan mostly will churn than stay subscription with the company.

Coming to machine learning models, I have used lazypredict library to evaluate many machine learning models at once. LGBM Classifier has the highest accuracy i.e. 95% and f1-score i.e. 96%. So, LGBM Claasifier is a good fit to predict Customer Churn. I also have used hyperparameter tunning with GridSearch to find the best parameter for LGBM Classifier to predict Customer churn. As we can see that hyperparameter tunning can increase precision score and this is very useful. So we will be confidence with our models to predict Data Test with unseen label (Churn).
