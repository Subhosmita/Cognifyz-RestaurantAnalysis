import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
url="https://drive.google.com/file/d/1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y/view?usp=drive_link"
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df=pd.read_csv(url)





#Task3: Price Range vs. Online Delivery and Table Booking
'''Analyze if there is a relationship between the
price range and the availability of online
delivery and table booking.'''

# to analyzed this we need to plot 2 charts together
x1 = df['Has Online delivery']
y = df['Average Cost for two']
x2 = df['Has Table booking']

# Plot 1 for Online Delivery with the avg cost 
# Plot 2 for Table Bokking with the avg cost 


plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
sns.boxplot(x=x1, y=y)
plt.xlabel('Online delivery')
plt.ylabel('Average Cost for two')
plt.title('Online delivery affected by cost')
plt.subplot(1,2,2)
sns.boxplot(x=x2,y=y)
plt.xlabel('Table booking')
plt.ylabel('Average Cost for two')
plt.title('Table booking affected by cost')
plt.tight_layout()
plt.show()

print(" Both the Online delivery and Table booking are negetively impacted by the cost")




'''Determine if higher-priced restaurants are
more likely to offer these services.'''

print("High priced Restaurants which have average cost more than 10,000 did not provide Online delivery as well as Table Booking facilities.")


#  let's check for the resturents have avg cost less than 10,000


plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
sns.boxplot(x=x1, y='Average Cost for two', data=df.loc[df['Average Cost for two']<10000 ] )
plt.title('Online delivery by cost')
plt.subplot(1,2,2)
sns.boxplot(x=x2, y='Average Cost for two', data=df.loc[df['Average Cost for two']<10000 ] )
plt.title('Table booking by cost')
plt.tight_layout()
plt.show()

print(" The Online delivery facility is present for only those resturent , where the avg cost is less than 1000. ")
print(" The Table booking facility is available in restaurants with an average cost ranging from 1000 to 2000. ")
