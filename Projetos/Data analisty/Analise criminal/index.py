import pandas as pd

database = pd.read_csv('model/database.csv')

df = pd.DataFrame(database)

print(df.tail())