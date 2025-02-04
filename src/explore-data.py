import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
data = pd.read_csv(url, sep = '\t')

# Print and show item price with $ sign and type of object
print(data.head())
data["item_price"]

# Define trans func
def data_transform(data):
    data["item_price"] = data["item_price"].str.replace("$", "").astype(float)
    return data

# Call trans func to remove $ signs and conver to float
data = data_transform(data)
data["item_price"]

print(data.head())

