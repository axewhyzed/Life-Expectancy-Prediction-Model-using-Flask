# Life-Expectancy-Predictor-using-Linear-Regression-and-Flask<br>

This project is a life expectancy prediction system that uses linear regression to predict life expectancy based on various factors such as adult mortality, alcohol consumption, percentage expenditure, Hepatitis B, Measles, Body Mass Index (BMI), Polio, total expenditure, Diphtheria, HIV/AIDS, Gross Domestic Product (GDP), population, income composition of resources, and schooling. The model is deployed on the web using Flask.<br>

# Code
The `linear_reg.py` script contains the code to generate the linear regression model. The script loads the Life Expectancy Data from a CSV file, drops unnecessary columns, and removes missing values. The remaining columns are used to train the linear regression model. The trained model is saved to a pickle file for later use.<br>

The `app.py` script contains the code for the Flask deployment server. The trained model is loaded from the pickle file and used to predict life expectancy based on the user's input values. The predicted value is displayed on the web page.<br><br>

# Usage
To use this life expectancy prediction system, clone the repository and run the Flask app using the following command:
```
python app.py
```
Then, navigate to http://localhost:5000 in your web browser. Enter the required input values and click on the "Predict" button. The predicted life expectancy value will be displayed on the screen.<br><br>

# Dataset<br>
The Life_Expectancy_Data.csv file used in this project is taken from [Kaggle](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who)<br><br>

# Contributing<br>
Contributions are always welcome! Please feel free to submit a pull request or open an issue if you find a bug or have a suggestion for improvement.

