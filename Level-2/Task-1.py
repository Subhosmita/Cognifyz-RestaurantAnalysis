import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url="https://drive.google.com/file/d/1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y/view?usp=drive_link"
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df=pd.read_csv(url)

#print(df.columns)
#Task1: Restaurant Ratings

'''Analyze the distribution of aggregate
   ratings and determine the most common
   rating range.'''

agg_rating_distribution=df['Aggregate rating'].value_counts()
print(agg_rating_distribution)


a=agg_rating_distribution.idxmax()
print("Most common rating range is : " ,a)

plt.hist(df['Aggregate rating'], bins=30, color='skyblue', edgecolor='black')
plt.xlabel("Aggregate rating")
plt.ylabel("Count")
plt.title("Distribution of aggregate rating")
plt.show()

'''Calculate the average number of votes
   received by restaurants.'''

avg_vote= round(df[ 'Votes'].mean(),3)
print("The average number of votes received by restaurants : ",avg_vote)

