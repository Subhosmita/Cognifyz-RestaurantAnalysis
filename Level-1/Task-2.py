import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url="https://drive.google.com/file/d/1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y/view?usp=drive_link"
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df=pd.read_csv(url)

# Task2: City Analysis

'''Identify the city with the highest number
   of restaurants in the dataset.'''

print(df.columns)



city_count = df['City'].value_counts()
restaurants_no = city_count.head(1)
print("City with the highest number of restaurants : ", city_count.idxmax())
print(restaurants_no)

'''Calculate the average rating for
   restaurants in each city.'''

rating_by_each_city= df.groupby('City')['Aggregate rating'].mean()
print("The average Rating of each city : ",rating_by_each_city)

'''Determine the city with the highest
   average rating.'''

top_rated_city=rating_by_each_city.idxmax()
value=rating_by_each_city.max()
print("The city With Highest Avg. Rating is : ",top_rated_city,",","Rating =",value)