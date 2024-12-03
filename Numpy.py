# Exercise 1

import numpy as np

# Creating the array and reshaping it
array = np.arange(1, 11).reshape(2, 5)
print(array)

# Exercise 2

# Creating the array and extracting the elements
array = np.arange(1, 21)
subset = array[5:16]  # Extracting elements from 5th to 15th index
print(subset)

#  Exercise 3

import pandas as pd

# Creating the series and adding a new item
series = pd.Series({'apples': 3, 'bananas': 2, 'oranges': 1})
series['pears'] = 4
print(series)

# Exercise 4

# Creating the dataframe
data = {
    "name": ["Person1", "Person2", "Person3", "Person4", "Person5",
             "Person6", "Person7", "Person8", "Person9", "Person10"],
    "age": [25, 30, 35, 28, 32, 26, 27, 31, 29, 33],
    "gender": ["Male", "Female", "Female", "Male", "Male",
               "Female", "Male", "Female", "Male", "Female"]
}
df = pd.DataFrame(data)
print(df)

# Exercise 5

# Adding a new column 'occupation'
occupations = ["Programmer", "Manager", "Analyst", "Programmer", "Manager",
               "Analyst", "Programmer", "Manager", "Analyst", "Programmer"]
df['occupation'] = occupations
print(df)

# Exercise 6

# Selecting rows where age is greater than or equal to 30
filtered_df = df[df['age'] >= 30]
print(filtered_df)

# Exercise 7

# Converting to CSV and reading it back
csv_path = "dataframe.csv"
df.to_csv(csv_path, index=False)  # Save to CSV file
loaded_df = pd.read_csv(csv_path)  # Read from CSV file
print(loaded_df)

