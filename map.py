import pandas as pd
df = pd.read_excel(r"C:\\Users\\aakan\\OneDrive\\Documents\\BE\\BDA\\Miniproj\\Data_Train.xlsx")
df['Date_of_Journey'] = pd.to_datetime(df['Date_of_Journey'])
df['month'] = df['Date_of_Journey'].dt.month
data = pd.DataFrame(df, columns=['Airline','Source','Destination','month','Price'])
print(type(data))
#agg = list(data.groupby(['month','Source','Destination']))
#print(agg)