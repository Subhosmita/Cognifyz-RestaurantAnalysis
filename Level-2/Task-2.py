import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url="https://drive.google.com/file/d/1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y/view?usp=drive_link"
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df=pd.read_csv(url)

#Task2: Cuisine Combination
'''Identify the most common combinations of
cuisines in the dataset.'''

common_combinations= df.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)
top10=common_combinations.head(10)
print("Top 10 most common combinations are : ",top10)



'''Determine if certain cuisine combinations
tend to have higher ratings.'''

max_rating = common_combinations.iloc[0]
print(max_rating)

max_rated_rest = df.loc[df['Aggregate rating'] == max_rating]
print("Restaurants having the maximum rating : ", max_rated_rest['Restaurant Name'])
