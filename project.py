
import numpy as np

import pandas

unemployment_data = pandas.read_csv('unemployment.csv')


import matplotlib.pyplot as plt

date_column = unemployment_data['Date']

all_column = unemployment_data['All']



df_all = unemployment_data['All'].replace('%',"",regex=True).astype('float')


print(df_all)

y = df_all

x = np.arange(463)

my_xticks = unemployment_data['Date']


plt.xticks(x, my_xticks)

plt.plot(x, y)

plt.xlabel('Date')
plt.ylabel('Unemployement rate (in %)')

plt.show()


