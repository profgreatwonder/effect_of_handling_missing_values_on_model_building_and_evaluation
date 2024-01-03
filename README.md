# Boston House Price Prediction

## Problem Statement

This project is about creating a model that will help users predict the house prices in Boston. For this model, we will check the effect of 4 different methods of handling missing values to see it's effect on the model in order to choose the best model based on how the missing values were handled.

The model that fared the best will then be passed to production for future prediction.

The dataset was split into two, `train` (which was further split in two, `train` and `validation`) and `test`.

Filling the missing values

- with 0s
- with the mean of the column
- by deleting the rows with missing data
- by deleting the columns with missing data

## Dataset Description

The dataset used for this project is from the housing market in Boston. The dataset contains 506 observations and 14 attributes.

1. CRIM: Per capita crime rate by town.
2. ZN: Proportion of residential land zoned for lots over 25,000 sq. ft.
3. INDUS: Proportion of non-retail business acres per town.
4. CHAS: Charles River dummy variable (1 if tract bounds river; 0 otherwise).
5. NOX: Nitric oxides concentration (parts per 10 million).
6. RM: Average number of rooms per dwelling.
7. AGE: Proportion of owner-occupied units built prior to 1940.
8. DIS: Weighted distances to five Boston employment centers.
9. RAD: Index of accessibility to radial highways.
10. TAX: Full-value property tax rate per 10k.
11. PTRATIO: Pupil-teacher ratio by town.
12. B: (1000(Bk - 0.63)^2), where (Bk) is the proportion of Black residents by town.
13. LSTAT: Percentage of lower status of the population.
14. MEDV: Median value of owner-occupied homes in $1000s (the target variable).

## Project Todos

1. Importing necessary libraries and loading dataset
2. Prepare and clean data
3. perform Exploratory Data Analysis (EDA)
4. Select key features (feature importance) using risk ratio, mutual information, correlation - lesson 3 and sql_tableau tutorial
5. Splitting the dataset
6. Building a linear model
7. Use Linear Regression to predict price
8. Residual Analysis of the train and val data
9. Evaluate the model using lesson 4 ml zoomcamp
10. Use the model on the test data
11. Pickle the model for deployment

## Software and Tools

1. VSCODE
2. Jupyter Notebook
3. Git/Github
4. Render for deployment

## Notebook Links

Each folder contains the dataset and model building notebook

- Model built with the deleted columns with missing values
- Model built with the deleted rows with missing values
- Model built with the replacing the missing values with the mean of the column they belong to
- Model built with the replacing the missing values with 0.00

## Replicating the Project

The environment was created, activated and requirements stored in yaml file by running the following commands:

##### for .yml

- conda create --name boston_house_pricing
- conda activate boston_house_pricing
- conda env export --no-builds > environment.yml

To replicate the environment, run the following commands:

- Clone the Project
- Create the environment and install all requirements by running the command:

      conda env create -f environment.yml

##### for .txt with conda

- conda create --name boston_house_pricing
- conda activate boston_house_pricing
- conda list --export > environment.txt

To replicate the environment, run the following commands:

- Clone the Project
- Create the environment and install all requirements by running the command:

      conda create --name <env_name> --file environment.txt

<!-- ##### for .txt with pip
- pip freeze > requirements.txt
- pip install -r requirements.txt -->

## Conclusion

I observed that it is wise to check the correlation and coefficient before deciding to delete the missing values. In this case, age was an important factor but it had to be deleted because it had missing values. I deleted column-wise and row-wise.

The model where the missing values were replaced with the mean fared better than the rest followed by ......

The first and ninth data point was to test the output of the prediction values

- Model built with the deleted columns with missing values
- Model built with the deleted rows with missing values
- Model built with the replacing the missing values with the mean of the column they belong to
- Model built with the replacing the missing values with 0.00

The evaluation metrics for all four include
