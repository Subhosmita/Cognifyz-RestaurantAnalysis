import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url="https://drive.google.com/file/d/1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y/view?usp=drive_link"
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df=pd.read_csv(url)


#  Task3: Price Range Distribution


print(df.columns)


'''Create a histogram or bar chart to
visualize the distribution of price ranges
among the restaurants.'''

df.hist(column="Price range")
plt.title('Distribution of Price Ranges')
plt.xlabel('Price Range')
plt.ylabel('Counts')
plt.show()



'''Calculate the percentage of restaurants
in each price range category.'''


price_range_count=df["Price range"].value_counts()
total_restaurant = len(df)
percentage = round((price_range_count/total_restaurant)*100,2)
percentage_m= pd.merge(price_range_count, percentage,on="Price range")
print("The %  of Resturent in each Price Range Category are : ",percentage_m)


plt.pie(percentage,labels=percentage.index,autopct='%1.1f%%',colors=["yellow","lightgreen","pink","silver"])
plt.title("Price range percentage ")
plt.show()
