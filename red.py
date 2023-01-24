from map import data
agg = data.groupby(['month','Source','Destination'])['Price'].apply(list)
#print(type(agg))
print(agg[1])