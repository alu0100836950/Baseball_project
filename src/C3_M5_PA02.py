#!/usr/bin/env python
# coding: utf-8

# # Automation and scripting with Python


# ## Scenario
# You are a Python developer tasked with gathering sports betting and baseball statistics. You will load a CSV file to a DataFrame, perform some analysis, and generate visualizations, as you have done in previous material. After the data is processed, you will set up SendGrid to send an email to your supervisor (using the sample code you've obtained from the SendGrid documentation). This is designed to send an alert once your analysis is done. You will add your API key and configure the message. 
# 
# You will add scheduling to a program so that the analysis is run every day and the automated email will be sent after completion of the analysis, and you will use file operations to save your DataFrame, ensuring you do not overwrite the previous set of data. As you do this, you will add logging messages where appropriate.
# 
# As you progress through this lab, you will use Git to manage your project and commit regularly.


# #### Step 1.2: Make Regular Commits
# Ensure that you commit your changes regularly using descriptive commit messages.


# ### 1. Data Handling and Preprocessing
# #### Step 2.1: Load the Dataset
# Load the provided sports dataset **sports_data_missing.csv** into a pandas DataFrame and inspect it to understand the structure, missing values, and any inconsistencies.


import pandas as pd

# Load the dataset
df = pd.read_csv('../data/sports_data_missing.csv')

# Display the first few rows
print(df.head())

# Display info about DataFrame
df.info()

#### Step 2.2: Clean and Preprocess the Data
#Check for missing or invalid values, and clean the dataset as needed (e.g., fill missing values, handle data inconsistencies). In this case, drop any columns with invalid data.

# Drop rows with invalid data
df = df.dropna()

# Inspect the cleaned data
df.info()

print("Data cleaning completed.")

### 3. Visualization Building and Evaluation
#### Step 3.1: Create Functions for Visualizations
# Create a function to generate different visualizations based on the dataset. For example, scatter plots showing player statistics. Please note these abbreviations:
# - HR = Home Runs
# - BB = Walks (Base on Balls)
# - SO = Strikeouts
# - AB = At Bats

# Some common examples of baseball metrics are a comparison of how many strikeouts (SO) vs. walks (BB), and number of at bats (AB) vs. home runs (HR). Create two scatter plots, one showing the Walk vs. Strikeout Ratio, and the second showing Home Runs vs. At Bats ratio.

# Create a function called create_scatter_plot that accepts the dataframe, the x and y column names, and the chart title, and generates and displays a scatter plot.

import matplotlib.pyplot as plt

# Function to create scatter plot
def create_scatter_plot(df, x_col, y_col, title):
    plt.figure(figsize = (10, 6)) # Figure size is provided
    # YOUR CODE HERE - Make the plot a scatter plot with the DataFrame's x_col and y_col as parameters
    plt.scatter(df[x_col], df[y_col])
    # YOUR CODE HERE - Set the plot title to the title parameter
    plt.title(title)
    # YOUR CODE HERE - Set the x_label to the x_col parameter
    plt.xlabel(x_col)
    # YOUR CODE HERE - Set the y_label to the y_col parameter
    plt.ylabel(y_col)
    # YOUR CODE HERE - # Switch gridlines on (True)
    plt.grid(True)
    plt.show()
    

# Example usage
create_scatter_plot(df, 'BB', 'SO', 'Walk (BB) vs Strikeout (SO) Ratio')
create_scatter_plot(df, 'HR', 'AB', 'Home Runs (HR) vs At Bats (AB) Ratio')


print("Visualizations created.")


#### Step 3.2:  Create a box plot
#Use Matplotlib to generate a box plot with singles, doubles, triples, and home runs. The X label should be Hits and the Y label should be Hit Type. The title should be Distribution of Hits.

# Create box plots using Matplotlib
plt.figure(figsize = (10, 6)) # Figure size is provided

# Set up data to contain the Singles, Doubles, Triples, and Home Runs from the DataFrame "df"
data = [df['Singles'], df['Doubles'], df['Triples'], df['HR']]

# Create the boxplot with specified options
plt.boxplot(data, vert=False, patch_artist=True) # Code is provided
plt.yticks(range(1, 5), ['Singles', 'Doubles', 'Triples', 'Home Runs']) # Code is provided
# YOUR CODE HERE - set xlabel to Hits
plt.xlabel('Hits')
# YOUR CODE HERE - set ylabel to Hit Type
plt.ylabel('Hit Type')
# YOUR CODE HERE - set title to Distribution of Hits
plt.title('Distribution of Hits')
# YOUR CODE HERE - # Switch gridlines on (True)
plt.grid(True)
plt.show()

#### Step 3.3:  Calculate averages and remove outliers
#Remove all players with 0 walks or 0 strikeouts, and create a new column "SO/BB" that calculates the strikeout to walk ratio. 
#Calculate the mean singles, doubles, triples, home runs (HR), and the minimum and maximum strikeout-to-walk ratio (SO/BB) from the column created in this step.

# Remove players with 0 walks from DataFrame
df = df[df['BB'] != 0]
print("Players with 0 Walks removed.")
print(df.info())

# Remove players with 0 Strikeouts from DataFrame
df = df[df['SO'] != 0]
print("Players with 0 Strikeouts removed.")
print(df.info())

# Create column with Strikeout/Walk Ratio %
df["SO/BB"] = df["SO"] / df["BB"]
print("Strikeout to Walk Ratio column created.")
print(df.head())

# Use DataFrame functionality to calculate the mean of the fields below

average_singles = df['Singles'].mean()  
average_doubles = df['Doubles'].mean()
average_triples = df['Triples'].mean()
average_hr      = df['HR'].mean()

# Use DataFrame functionality to calculate the max and min of the strikeout to walk ratio
max_SO_BB = df['SO/BB'].max()
min_SO_BB = df['SO/BB'].min()

# Checking Your Results:
print(f"Singles: {average_singles}")
print(f"Doubles: {average_doubles}")
print(f"Triples: {average_triples}")
print(f"Home Runs: {average_hr}")