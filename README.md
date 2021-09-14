# Flask-Model-deployment-Advertising-Sales-Prediction

This is a Machine learning Model deployment project.
I have taken a problem statement which aims to predict the sales data based on the input features giving the amount spent on the different categories of advertising.

# Data:
Independant variables:- 
* 1.TV	- Amount spent on T.V. Ads
* 2.Radio	- Amount spent on Radio Ads
* 3.Newspaper - Amount spent on Newspaper Ads

Dependant variable/ Output:
* Sales - Sales revenue generated 

# Methodology used:
* I have used Random Forest Regressor algorithm for this usecase to train on the i/p data and predict the future sales for new advertising data.
* Then I deployed the modelusing Flask on my of local computer(localhost).
* Finally tested the API using Postman to perform the POST & GET requests to predict the sales for new incoming data of advertising expenditure.
