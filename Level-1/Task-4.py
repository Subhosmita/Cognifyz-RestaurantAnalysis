import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url="https://drive.google.com/file/d/1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y/view?usp=drive_link"
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df=pd.read_csv(url)

#Task4: Online Delivery
'''Determine the percentage of restaurants
that offer online delivery.'''

print(df.columns)


online_delivery= df['Has Online delivery'].value_counts().get('Yes', 0)
print("Total Resturent with Online Delivery : ",online_delivery)

no= df['Has Online delivery'].value_counts().get('No', 0)
print("Resturent with NO Online Delivery : ",no)

Row_count= len(df)
percentage_of_online_delivery= round((online_delivery/Row_count)*100,2)
print("ToTal % of Online Delivery :", percentage_of_online_delivery)

percentage_of_NO_online_delivery =round((no/Row_count)*100,2)
print("Total % where Online Delivery is not present : ",percentage_of_NO_online_delivery)


'''Compare the average ratings of restaurants
with and without online delivery.'''

Avg_rating_yes= round(df[df['Has Online delivery'] == 'Yes']['Aggregate rating'].mean(),2)
print("Average Rating With online Delivery : ",Avg_rating_yes)

Avg_rating_No= round(df[df['Has Online delivery'] == 'No']['Aggregate rating'].mean(),2)
print("Average Rating Without online Delivery : ",Avg_rating_No)

labels = ['YES', 'NO']
average_rating = [Avg_rating_yes, Avg_rating_No]
colors='green','yellow'
plt.barh(labels, average_rating, color=colors)
plt.ylabel('Online Delivery')
plt.xlabel('Average Rating')
plt.title('Comparison of Average Ratings of Online delivery')
plt.show()
