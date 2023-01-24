import pandas as pd
import seaborn as sns
import numpy as np
import pylab as plt
df = pd.read_excel(r"C:\\Users\\aakan\\OneDrive\\Documents\\BE\\BDA\\Miniproj\\Data_Train.xlsx")
#data = pd.DataFrame(df,columns=)
df['Date_of_Journey'] = pd.to_datetime(df['Date_of_Journey'])
df['Date_of_Journey'] = df['Date_of_Journey'].dt.month
#No of flights in each month
#months = df.Date_of_Journey.value_counts()
#sns.barplot(x=months.index, y=months.values)
#plt.show()

#No of flights of each airline
airline = df.Airline.value_counts()
#print(airline)
plt.figure(figsize=(18,4))
sns.barplot(x=airline.index, y=airline.values)
plt.xticks(rotation=45, fontsize=8)
plt.show()