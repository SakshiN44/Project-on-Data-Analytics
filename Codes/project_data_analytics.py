# -*- coding: utf-8 -*-
"""Project: Data_Analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y32aAYxVmE4BD8XoYi-OPHis60GE8oU6

# STW Final Project
# Name: Sakshi Nimje (VIIT, PUNE)
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline
df1 = pd.read_csv("datasets_india.csv")
df2 = pd.read_csv("datasets_USA.csv")
print(df1)
print(df2)

# Removing the unwanted columns (Data Cleaning)
df_india = df1.drop(['country','county','type','measure','source','source_url'], axis = 1)
print(df_india)
df_usa = df2.drop(['country','measure','source_url'], axis = 1)
print(df_usa)

# General statistics using central tendencies 
# Central tendencies include mean, median, and mode

# Regarding USA
print("Mean of beds in USA:",df_usa.beds.mean())
print("Median of beds in USA:",df_usa.beds.median())
print("Corrected data:\n",df_usa.corr())

# General statistics using percentages 
# Including count, mean, standard deviation, min and max value, and the percentages in terms of 25%,50%,75%
print(df_usa.describe())

# Regarding INDIA
print("Mean of beds in India:",df_india.beds.mean())
print("Median of beds in India:",df_india.beds.median())
print("Corrected data:\n",df_india.corr())

# General statistics using percentages 
# Including count, mean, standard deviation, min and max value, and the percentages in terms of 25%,50%,75%
print(df_india.describe())

"""# Info regarding INDIA

#Bar Graph of STATE v/s BEDS in INDIA
"""

import matplotlib
matplotlib.style.use('ggplot') # Changing Styles of plot

#Adding Title
plt.title('Bar Graph of STATE v/s BEDS in INDIA')

# Graph between State v/s Beds
plt.rcParams['figure.figsize']=(20,15)
plt.bar(df_india.state,df_india.beds)

# X-axis label
plt.xlabel('Initials of States')
# Y-axis Label
plt.ylabel('Number of Beds')

"""# Conclution of Above Graph
# We can conclude that the state Tamil Nadu (TN) has highest number of beds in comparison with other states of India.

# Bar Graph of YEARS v/s BEDS in INDIA
"""

import matplotlib
matplotlib.style.use('ggplot') # Changing Styles of plot

#Adding Title
plt.title('Bar Graph of YEARS v/s BEDS in INDIA')

#year vs beds
plt.bar(df_india.year,df_india.beds)

# X-axis label
plt.xlabel('YEARS')
# Y-axis Label
plt.ylabel('Number of Beds')

"""# Conclution of Above Graph
# We can conclude that in the year 2017 there were maximum number of beds in all over India.

#Bar Graph of State v/s Population in INDIA
"""

import matplotlib
matplotlib.style.use('ggplot') # Changing Styles of plot

#Adding Title
plt.title('Bar Graph of State v/s Population in INDIA')

#State vs Population (INDIA)
plt.rcParams['figure.figsize']=(20,8)
plt.bar(df_india.state,df_india.population)

# X-axis label
plt.xlabel('STATES')
# Y-axis Label
plt.ylabel('Population in India')

"""# Conclution of Above Graph
# We can conclude that the State IN has the highest population in comparison with other states.

# Info about USA

# Bar Graph of STATE v/s BEDS in USA
"""

import matplotlib
matplotlib.style.use('ggplot') # Changing Styles of plot

#Adding Title
plt.title('Bar Graph of STATE v/s BEDS in USA')

# Graph of State v/s Beds in USA
plt.rcParams["figure.figsize"] = (20,8)
plt.bar(df_usa['state'],df_usa['beds'])

# X-axis label
plt.xlabel('Initials of States')
# Y-axis Label
plt.ylabel('Number of Beds in USA')

"""# Conclution of bove Graph
# We can conclude that In USA Kansa (KS) has maximum number of beds followed by Iowa(IA). Texas(TS) and Florida(FL) has comperatively similar number of beds.
# In comparison with India, USA has a qual number of distribution of beds in their states.

#Bar Graph of TYPE of BEDS v/s Number of BEDS
"""

import matplotlib
matplotlib.style.use('ggplot') # Changing Styles of plot

#Adding Title
plt.title('Bar Graph of TYPE of BEDS v/s No of BEDS')

#type vs bed
plt.rcParams["figure.figsize"] = (20,8)
plt.bar(df_usa['type'],df_usa['beds'])

# X-axis label
plt.xlabel('TYPES')
# Y-axis Label
plt.ylabel('Number of Beds')

"""# Conclution
# We can conclude that the types of beds in USA has maintained. Acute beds has maximum number of count, followed by Psychiatric. ICU beds have a count of more than 30. However there are just 10 count of other types of bed.
# In comparison with India USA has maintained the types of bed with a decent count

#Bar Graph of State v/s Population in USA
"""

import matplotlib
matplotlib.style.use('ggplot') # Changing Styles of plot

#Adding Title
plt.title('Bar Graph of State v/s Population in USA')

#State vs Population(USA)
plt.rcParams["figure.figsize"] = (20,8)
plt.bar(df_usa['state'],df_usa['population'])

# X-axis label
plt.xlabel('STATES')
# Y-axis Label
plt.ylabel('Population in USA')

"""#Conclution
# We can conclude that California has the highest population in United States as compared to others.
#In comparison with India USA has almost an equal level of diatribution of population.

# Pie chart on DATA SOURCE
"""

import matplotlib
matplotlib.style.use('ggplot') # Changing Styles of plot

#a pie chart on data source
df_usa['source'].unique()
rr = ['khn','arcgis']
df_usa['source'].value_counts()
oc = [2301,3412]
plt.pie(oc,labels=rr,autopct='%1.1f%%', radius=1, explode=[0,0.1])

plt.show()

"""# Conclution
# Above is a pie chart of data source which shows distribution of khn and arcgis.
"""