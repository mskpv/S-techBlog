import pandas as pd

data = pd.read_csv('mask.csv')

# read row line by line
for d in data.values:
      # read column by index
        print(d[2],d[3])
