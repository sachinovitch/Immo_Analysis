# Immo_Analysis
With the goal of predicting prices of the Belgian real estate market, a regression-model is created, trained on data scraped from Belgian immo websites. The model can take property information as input and will return a price-prediction as output.

## Description
Using a dataset containing almost 12000 rows of Belgian properties for sale with 21 columns of feature information, graphs are made to visualize certain trends and patterns of the real estate market.  
The features with significant corealations to the price are then used as parameters to train the regression-models. There are 3 versions of the model using different approaches; linear regression, decision-tree and neural network.



## Instructions
You can find the code for cleaning and visualizing the data in the file called 'Immo_analysis.ipynb'. By chronologically running the codeblocks, output will be presented by DataFrames and Plots.  
To use the model for predicting the price of a property in Belgium, follow these steps:  
-   Activate the virtual envirement:
    -   In ps1: cd ./Immo_Analysis
    -   In ps1: /Immo_Analysis/Immo_Analysis/venvImmoAPI/Scripts/Activate.ps1
-   Run the file preprocessing.py
-   Run the file app.py
-   Activate the interactive API:
    -   In CMD: python -m uvicorn app:app --reload
After these steps the API-model is available on http://127.0.0.1:8000/docs

## Folder Structure
```
.
└── Immo_Analysis/
    ├── data/
    │   └── _output.csv
    ├── src/
    │   └── preprocessing.py
    ├── models/
    │   └── decission_tree.pickle
    ├── model-building/
    │   └── pipeline.py
    ├── notebooks/
    │   └── ImmoAnalysis.ipynb
    │   └── regression-models.ipynb
    ├── output/
    │   └── matplotlib plots as .png
    ├── .gitignore
    ├── app.py
    └── README.md

```


## Case
#### Data-cleaning
The dataset obtained by scraping required the following data-cleaning steps:   
-   Reordering the columns
-   Converting the columns of the DataFrame to a desired datatype
-   Removing duplicates
-   Removing leading and trailing spaces
-   Remove rows with specific errors
#### Data-exploration
The visualization of the data for analysis is focused on comparing the relations between price, total property area, house type and province.  
The data shows this distribution of property-value(€/m²) across Belgium:
![](output/Price%20per%20Property%20Area.png)
![](output/Price%20per%20Area%20by%20Province%20and%20Type%20(with%20Outliers%20Incorporated).png)


#### Model-building  
Before creating a pipeline for the model, the data is preprocessed to obtain suitable features to train a ML-model. After evaluation of different models, the regression-tree model has been chosen to complete the pipeline.


