Prediction of Coronary Heart Disease in the next ten years

Project Summary

Heart disease is a generic term used to represent all conditions that affect the structure and functioning of the heart. Coronary heart disease (CHD) is a specific type of heart disease and in USA alone there are around 18.2 million people with CHD. CHD is a severe problem and detecting the presence of it in the earlier stages would help the person get cured or do not let it become serious by changing their lifestyle, medicine, surgery etc. 

Hence this project is to predict and identify the prospective patients by a robust model, then hospitals and clinics can use that model to identify undiagnosed patients who are at risk for the disease. This can improve the spending for the patient and improve the quality of life as well.

The data will be cleaned by replacing the missing values and then correlation matrix is created using point-biserial correlation as our dataset has a mixture of continuous and binary variables. Data will be split into training and test data in the ratio of 80% to 20% where the Target is the Ten-Year CHD - Indicator that signifies if the partient will suffer from CHD in the next 10 years. 

Decision Tree Classifier performed well compared to Logistic Regression and Random Forest Classifier models. So we went ahead with Decision Tree Classifier and tuned that further using MinMaxScaler and SMOTE. The final Decision Tree Classifier model with resample dataset on the scaled data of the original dataset has yielded the best results and will be used to go ahead with implementation. 

Dataset - https://www.kaggle.com/datasets/jiantay33/coronary-prediction
