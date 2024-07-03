import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url="https://drive.google.com/file/d/1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y/view?usp=drive_link"
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df=pd.read_csv(url)

# Task1: Top Cuisines
'''Determine the top three most
   common cuisines in the dataset.'''

print(df.shape)
print(df.columns)

print(df['Cuisines'])


cuisine_count= df['Cuisines'].str.split(', ').explode('Cuisines').value_counts()
print(cuisine_count)
top_cuisine=cuisine_count.head(3)
print("The Top 3 Cuisines are : ",top_cuisine)


colours = ['green', 'orange', 'red']
plt.bar(top_cuisine.index, top_cuisine.values, color=colours)
plt.xlabel('Cuisine')
plt.ylabel('Count')
plt.title('Top Three Cuisines')
plt.show()

'''Calculate the percentage of
  restaurants that serve each of the top
  cuisines.'''

total_restaurant = len(df)
print(total_restaurant)
top_cuisine10=cuisine_count.head(10)
percentages = (top_cuisine10 / total_restaurant) * 100
print("The Market share of Top 10 Cuisines are : ",percentages)

plt.bar(top_cuisine10.index, percentages.values, color=colours)
plt.xlabel('Cuisine Name')
plt.ylabel('Percentage')
plt.title('Top Ten Cuisines %')
plt.figure(figsize=(12,6))
plt.show()
