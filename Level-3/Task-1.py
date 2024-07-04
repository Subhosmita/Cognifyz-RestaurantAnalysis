import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url="https://drive.google.com/file/d/1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y/view?usp=drive_link"
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df=pd.read_csv(url)


print(df['Rating text'])

#  Task1: Restaurant Reviews
'''Analyze the text reviews to identify the most
   common positive and negative keywords.'''

positive_data = df.loc[df['Aggregate rating'] >= 2.5]
print(positive_data)


positive_keywords = positive_data['Rating text'].unique()
print(positive_keywords)

plt.hist(positive_data['Rating text'], label=positive_keywords)
plt.show()

negative_data = df.loc[(df['Aggregate rating'] < 2.5) & (df['Aggregate rating'] > 0)]
# print(negative_data)
negative_keywords = negative_data['Rating text'].unique()
print(negative_keywords)

plt.hist(negative_data['Rating text'], label=negative_keywords)
plt.show()


