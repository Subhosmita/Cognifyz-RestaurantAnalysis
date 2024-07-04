import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
url="https://drive.google.com/file/d/1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y/view?usp=drive_link"
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df=pd.read_csv(url)



#Task: Votes Analysis
'''Identify the restaurants with the highest and
   lowest number of votes.'''

Highest_voted_resturant = df.groupby('Restaurant Name')['Votes'].sum().sort_values(ascending=False)
Highest_voted_resturant= Highest_voted_resturant.idxmax()
print("The Highest Voted Resturent is : ",Highest_voted_resturant)

lowest_rated_resturant= df.groupby('Restaurant Name')['Votes'].sum().sort_values()
lowest_rated_resturant=lowest_rated_resturant.idxmin()
print("The Lowest Voted Resturent is : ",lowest_rated_resturant)


'''Analyze if there is a correlation between the
   number of votes and the rating of a
   restaurant.'''

corelation=np.corrcoef(df['Votes'],df['Aggregate rating'])
corelation=np.round(corelation,2)
print(corelation)


plt.figure(figsize=(10,5), dpi =100)
sns.heatmap(corelation,annot=True,fmt=".2f", linewidth=.4)
plt.show()

sns.scatterplot(data=df , y = 'Votes' , hue = 'Aggregate rating' , x = 'Aggregate rating' )
sns.regplot(data=df, x='Aggregate rating', y='Votes', scatter=False)
plt.title(f"Correlation between Aggregate rating and Votes: 0.31")
plt.show()
print("As per result corelation value = 0.31 , which indicates there is a moderate positive corelation between these two variables.")
