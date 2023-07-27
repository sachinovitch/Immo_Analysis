# Immo_Analysis
With the goal of predicting prices of the Belgian real estate market, a regression-model is created, trained on data scraped from Belgian immo websites.

## Description
Using a dataset containing almost 12000 rows of Belgian properties for sale with 21 columns of feature information, graphs are made to visualize certain trends and patterns of the real estate market.  
The features with significant corealations to the price are then used as parameters to train the regression-models. There are 3 versions of the model using different approaches; linear regression, decision-tree and neural network.


## Instructions
You can find the code for cleaning and visualizing the data in the file called 'Immo_analysis.ipynb'. By chronologically running the codeblocks, output will be presented by DataFrames and Plots.
To only see the visuals, you can take a look at the file called 'Visuals'. In there you will find all the plotted charts as png-files.

## Folder Structure
└── Immo_Analysis  
   ├── data/  
   │      └── _output.csv    
   ├── data-exploration/  
   │      └── notebook for cleaning and visualizing the data  
   ├── model-building/  
   │      └── notebook for modeling and further analysis  
   ├── output/  
   │      └── plotted charts as '.png'-files  
   └── README.md

## Case
#### Data-cleaning
The dataset obtained by scraping required the following data-cleaning steps:   
-   Reordering the columns
-   Converting the columns of the DataFrame to a desired datatype
-   Removing duplicates
-   Removing leading and trailing spaces
-   Remove rows with specific errors
#### Data-exploration
The visualization of the data for analysis is focused on comparing the relations between price, total property area, house type and province:  
These are the plotted charts:
-   Barchart: 'Average Price per Province'
-   Barchart: 'Property-Area/Price per Province in EU/m²'
-   Barchart: 'Average Price per Province with Deviation'
-   Histogram: 'Histogram of Prices'
-   Barchart: 'Average Price per Type of House'
-   Barchart: 'Average price per Type of Apartement'
-   Scattergraph: 'Price per Property Area'
-   Scattergraph: 'Price per Property Area by Province'
-   Boxgraph: 'Price per Area by Province'
-   Boxgraph: 'Price per Area by Province and Type'
-   Boxgraph: 'Price per Area for Highest and Lowest Postal Codes by Province'
-   Boxgraph: 'Price per Area by Province and Type (with Outliers Incorporated)'
-   Boxgraph: 'Price per Area by Province and Type (with Highest and Lowest Municipality)'
#### Model-building  
Before creating a pipeline for the regression model, the data is preprocessed to obtain suitable features in the following steps:  
-   converting the 'province'-column and the 'subtype of property'-column to binary columns

