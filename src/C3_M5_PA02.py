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
df = # YOUR CODE HERE - load sports_data_missing CSV file into the DataFrame

# Display the first few rows
print(df.head())

# Display info about DataFrame
df.info()

