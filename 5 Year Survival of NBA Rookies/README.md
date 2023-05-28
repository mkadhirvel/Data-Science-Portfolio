5 Year Survival of NBA Rookies

Project Summary

Rookies are professional athletes in their first year and NBA draft is used to add rookies to their teams. For any rookie player who are part of the first round of the NBA draft, contract is of 2 years with full guarantee and the 3rd and 4th years being options. Other players as part of their draft have their contract from 1 to 4 years with no guarantees.

For a team to be successful they need to identify rookie players who will benefit them in the long term. This is one of the most important questions to be answered before every season and I am going to utilize Data Analytics to try and answer this problem. Using the dataset available that lists the rookie year statistics I am going to build a predictive model that would carry out the analysis on whether a rookie NBA player will last 5 or more years in the league as the average career length of an NBA player is 4.5 years.

We will drop unneeded attributes and then correlation matrix is created to find the relationship between various variables. Data will be split into training and test data in the ratio of 80% to 20% where the Target is the target variable - Indicator that signifies if the NBA rookie makes it to 5 years and above in the league.

Random Forest Classifier performed well compared to Logistic Regression/KNN/Support Vector Machine models. So we went ahead with Random Forest Classifier that yielded the best results and will be used to go ahead with implementation. 

Dataset - https://www.kaggle.com/datasets/mamadoudiallo/5-year-survival-of-nba-rookies-from-19802015
