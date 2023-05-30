Movies Data Analysis

Project Summary

In this project we are using the TMDB 5000 Movies dataset and OMDBAPI and Wikipedia link of highest grossing films to collect more information about the various movies and the correlation between the various parameters. 

For all the input formats of API/CSV/WEB files we drop unnecessary columns, find duplicates, identify outliers etc. Then we combine the datasets into an SQLite table via SQL JOINS and then put it into a pandas data frame and create data visualizations.

TMDB 5000 Movie Dataset from Kaggle and this has various data about top 5000 movies. We will analyse some key variables to perform Exploratory Data Analysis (EDA) and find the relationship between budget and revenue of the top five thousand movies. 

We were able to use that information to visualize the data and arrive at conclusions like how budget of a movie affects the revenue. We were able to see that budget and runtime are more connected than budget and revenue which has more outliers.