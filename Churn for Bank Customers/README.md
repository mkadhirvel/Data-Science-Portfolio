Churn for Bank Customers

Project Summary

I have always wondered how businesses retain customers and in the case of banks with so many options available, retention of existing customers takes a vital role in keeping the banks profitable. I come from a Financial Sector background and know that retaining customers and increasing their lifetime value is one of the most important aspects of profitability. Churn is defined as a degree of customer inactivity over a given time. So, predicting churn is an important aspect of this when customer feedback is absent.

For a bank to be successful they need to retain existing customers and be on the lookout for any new customers. Acquiring new customers are costlier than retaining existing customers so this is a crucial factor. So, if we can predict that an existing customer might potentially leave the bank, we can develop loyalty programs to retain those customers. I am going to use Data Analytics to build a predictive model that would analyse and predict whether a customer would leave the bank or not based on the available features.

We will drop unneeded attributes and the create dummy variables for the existing categorical variables of Geography and Gender. Data will be split into training and test data in the ratio of 80% to 20% where the Target is the Exited variable - Indicator that signifies whether the customer left the bank or not.

Random Forest Classifier performed well compared to Logistic Regression/KNN/Support Vector Machine models. We applied MinMaxScaler on the Random Forest Classifier model which increased the accuracy further and so we went ahead with MinMaxScaler applied Random Forest Classifier that yielded the best results and will be used to go ahead with implementation. 

https://www.kaggle.com/datasets/mathchi/churn-for-bank-customers
