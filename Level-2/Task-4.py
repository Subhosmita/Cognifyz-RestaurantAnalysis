import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url="https://drive.google.com/file/d/1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y/view?usp=drive_link"
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df=pd.read_csv(url)



#Task: Restaurant Chains

'''Identify if there are any restaurant chains
   present in the dataset.'''

restaurant_chain = df.groupby("Restaurant Name").size().reset_index(name="OutletCount")
new = restaurant_chain[restaurant_chain["OutletCount"] > 1]
restaurant_chains = new.sort_values(by="OutletCount", ascending=False)

print(restaurant_chains[["Restaurant Name", "OutletCount"]].head(10))


plt.bar(restaurant_chains["Restaurant Name"][:5], restaurant_chains["OutletCount"][:5])
plt.xlabel("Restaurant Chain")
plt.ylabel("Number of Outlets")
plt.title("Top 5 Restaurant Chains by Number of Outlets")
plt.show()




'''Analyze the ratings and popularity of
    different restaurant chains.'''



ratings = df.groupby("Restaurant Name")["Aggregate rating"].mean().reset_index(name="Average Rating").sort_values(by="Average Rating", ascending=False)
print(ratings)


votes = df.groupby("Restaurant Name")["Votes"].sum().reset_index(name="Total Votes").sort_values(by="Total Votes", ascending=False)
print(votes)




plt.bar(ratings["Restaurant Name"][:5], ratings["Average Rating"][:5])
plt.figure(figsize=(10, 6))
plt.xlabel("Restaurant Chain")
plt.ylabel("Average Rating")
plt.title("Top 5 Restaurant Chains by Average Rating")
plt.show()



plt.bar(votes["Restaurant Name"][:5], votes["Total Votes"][:5])
plt.figure(figsize=(10, 6))
plt.xlabel("Restaurant Chain")
plt.ylabel("Total Votes")
plt.title("Top 5 Restaurant Chains by Total Votes")
plt.tight_layout()
plt.show()




