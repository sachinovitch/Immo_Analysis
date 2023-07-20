# Immo_Analysis
Analizing data of properties from Belgium, with the goal of making price-predictions for Immo Eliza, using visualized data.
## Description
Using the previously scraped dataset, containing almost 12000 rows of Belgian properties for sale with 21 columns of data in a csv-file, graphs are made to visualize certain trends and patterns of the real estate market.
## Instructions
You can find the code for cleaning and visualizing the data in the file called 'Immo_analysis.ipynb'. By chronologically running the codeblocks, output will be presented by DataFrames and Plots.
To only see the visuals, you can take a look at the file called 'Visuals'. In there you will find all the plotted charts as png-files.

## Case
The dataset obtained by scraping a Belgian immo-website did not require much data-cleaning
Data-cleaning steps:
    *   Reordering the columns
    *   Converting the columnss of the DataFrame to a desired datatype
    *   Removing duplicates
    *   Removing leading and trailing spaces
    *   Remove rows with specific errors

The visualization of the data for analysis is focused on comparing the relations between price, total property area, house type and province.
These are the plotted charts:
    *   Barchart: 'Average Price per Province'
    *   Barchart: 'Property-Area/Price per Province in EU/m²'
    *   Barchart: 'Average Price per Province with Deviation'
    *   Histogram: 'Histogram of Prices'
    *   Barchart: 'Average Price per Type of House'
    *   Barchart: 'Average price per Type of Apartement'
    *   Scattergraph: 'Price per Property Area'
    *   Scattergraph: 'Price per Property Area by Province'
    *   Boxgraph: 'Price per Area by Province'
    *   Boxgraph: 'Price per Area by Province and Type'
    *   Boxgraph: 'Price per Area for Highest and Lowest Postal Codes by Province'
    *   Boxgraph: 'Price per Area by Province and Type (with Outliers Incorporated)'
    *   Boxgraph: 'Price per Area by Province and Type (with Highest and Lowest Municipality)'
