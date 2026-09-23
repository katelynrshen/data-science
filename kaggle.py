# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # pip install numpy on console if you haven't done so
import seaborn as sns
import pandas as pd # pip install pandas on console if you haven't done so
import seaborn as sns
import matplotlib.pyplot as plt

#RUN THIS CELL TO INSTALL THE NEEDED PACKAGES AND LOAD THE DATAFRAME

df = pd.read_csv("AVDS 2026-2027 - Week 3 Data Student Copy")

df.drop('LotArea - delete', axis=1, inplace=True)

#Week 7:


#Slide 5: print the first 5 rows, last 5 rows, and DataFrame info



#Slide 8: there is one column that has too many decimal places - round them down so that the values are a whole number.
  #There is also a column with unnecessary whitespaces - remove those using one of the commands.
  #Find these two columns and write the code below



#Slide 16: Import pandas and read the housing data csv file into a DataFrame.
  #Display the first 5 rows of the dataset.
  #Print the list of columns and the shape of the DataFrame.
  #Convert the entire DataFrame into a numpy array
  #Use the numpy commands we learned to:
  #sort the array by house price, starting at least and ending at the greatest
  #hint: use .argsort() to sort by ascending order
  #write the code below




#Slide 18: return indices in the house price column where the house price is an outlier
  #Hint: outliers can be calculated using:
  #low outliers: First quartile - 1.5(Third Quartile - First Quartile)
  #high outliers: Third quartile + 1.5(Third Quartile - First Quartile)
  #Use google to find out how to calculate the first and third quartiles
  #fill in null values in the column that has null values
  #First determine the shape of the data in the column (skewed or symmetric)
  #if skewed, use median to fill the null values
  #if symmetric, use mean to fill the null values
  #write the code below


