# The Effect of 4 Different Methods of Handling Missing Values on Model Building and Evaluation

## Project Goal

The focus of the project is about checking the effect of 4 different methods of handling missing values to see how it affects model building and evaluaton.

## Project Desciption

Dataset will be prepared, cleaned and Exploratory Data Analysis(EDA) carried out in a file called, `data_preprocessing.ipynb`. From this file, 4 new datasets will be created after applying the different 4 different methodology of handling missing values. The generated datasets will then be used to build 4 models respectively. These models will be evaluated and based on the result of the evaluations, the best model will be selected. The selected model will the be passed to production(deployed).

The dataset was split into two, `train` and `test`. `train` would have been split further in two, `train` and `validation` but the dataset had just `506` observations.

#### Chosen Methodology for Handling Missing values

- with 0s
- with the mean of the column
- by deleting the rows with missing data
- by deleting the columns with missing data

#### The Evaluation Metrics for all Four Include:

- mean_absolute_error
- mean_squared_error
- mean_squared_error_with_np
- r2_score
- adjusted_r_score

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
4. Docker
5. Render for deployment

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

#### Note

In case you run into issues replicating the project due to how old it is (this works for any old project), After cloning, follow the steps provided:

1.  There is a need to generate a new requirement.yml or requirement.txt file which is named req.yml in my case:

         conda env export --no-builds > req.yml

2.  The generated yml file should then be edited at the top and the bottom

    - at the top, just before channels, a name has to be provided for enviroment. In my case, it is:

          name: missing_value_evaluation

    - at the bottom, the last line after dependencies, the prefix also has to updated with the filepath to your project which you can get from running the _pwd_ command.

3.  finally, create an environment from the edited yml file:

         conda env create -f req.yml

<!-- ##### for .txt with pip
- pip freeze > requirements.txt
- pip install -r requirements.txt -->

## Summary of Findings

After creating models and evaluating them, the model whose missing values were replaced zeros faired better than the other models. Below is a table that summarizes the result of the evaluation for each model:

- Model built with the deleted columns with missing values(dcmv)
- Model built with the deleted rows with missing values(drmv)
- Model built with the replacing the missing values with the mean of the column they belong to(rmvmm)
- Model built with the replacing the missing values with 0.00(rmz)

<table>
 <tr>
    <th>Model Name</th>
    <th>mean_absolute_error</th>
    <th>mean_squared_error</th>
    <th>mean_squared_error_with_np</th>
    <th>r2_score</th>
    <th>adjusted_r_score</th>
 </tr>
 <tr>
    <td>dcmv</td>
    <td>3.6454950179298584</td>
    <td>24.538442517765194</td>
    <td>4.9536292269168865</td>
    <td>0.7322723273710499</td>
    <td>0.7211939409174382</td>
 </tr>
 <tr>
    <td>drmv</td>
    <td>3.501122961969476</td>
    <td>22.85770809860834</td>
    <td>4.780973551339553</td>
    <td>0.7147470620507681</td>
    <td>0.6824542766225532</td>
 </tr>
 <tr>
    <td>rmvmm</td>
    <td>3.5384305807172383</td>
    <td>22.074466560695623</td>
    <td>4.698347215851083</td>
    <td>0.7591556370155939</td>
    <td>0.7383633179090264</td>
 </tr>
 <tr>
    <td>rmz</td>
    <td>3.392786788751625</td>
    <td>21.071458190983513</td>
    <td>4.590365801434948</td>
    <td>0.7700990005259702</td>
    <td>0.7502514322260541</td>
 </tr>
</table>

Below is the table to summarize the prediction done with each model................START HERE NEXT

<table>
 <tr>
    <th>Model Name</th>
    <th>mean_absolute_error</th>
    <th>mean_squared_error</th>
    <th>mean_squared_error_with_np</th>
    <th>r2_score</th>
    <th>adjusted_r_score</th>
 </tr>
 <tr>
    <td>dcmv</td>
    <td>3.6454950179298584</td>
    <td>24.538442517765194</td>
    <td>4.9536292269168865</td>
    <td>0.7322723273710499</td>
    <td>0.7211939409174382</td>
 </tr>
 <tr>
    <td>drmv</td>
    <td>3.501122961969476</td>
    <td>22.85770809860834</td>
    <td>4.780973551339553</td>
    <td>0.7147470620507681</td>
    <td>0.6824542766225532</td>
 </tr>
 <tr>
    <td>rmvmm</td>
    <td>3.5384305807172383</td>
    <td>22.074466560695623</td>
    <td>4.698347215851083</td>
    <td>0.7591556370155939</td>
    <td>0.7383633179090264</td>
 </tr>
 <tr>
    <td>rmz</td>
    <td>3.392786788751625</td>
    <td>21.071458190983513</td>
    <td>4.590365801434948</td>
    <td>0.7700990005259702</td>
    <td>0.7502514322260541</td>
 </tr>
</table>

## Conclusion

I observed that it is wise to check the correlation and coefficient before deciding to delete the missing values. In this case, age was an important factor but it had to be deleted while working on the model that used the dataset where the columns with missing values had to be deleted.

After comparing the results from the evaluation metrics and predictions with different values, it was observed that the model where the missing values were replaced with zeros fared better than the rest followed by ......

The first and ninth data point was to test the output of the prediction values

- Model built with the deleted columns with missing values
- Model built with the deleted rows with missing values
- Model built with the replacing the missing values with the mean of the column they belong to
- Model built with the replacing the missing values with 0.00

The evaluation metrics for all four include

## Challenges

The greatest challenge was not having `pickle` or its variant `dill` work for the project, it kept returning that `pickle` was not found. I finally went for the `joblib` which comes installed with the `scikit-learn` library.
