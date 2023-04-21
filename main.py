import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url="https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
tesla_revenue = pd.read_html(url)[1]

tesla_revenue.columns=['Date','Revenue']
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace(',','').str.replace('$','')
avg_revenue=tesla_revenue['Revenue'].astype('float').mean(axis=0)/200
tesla_revenue['Revenue'].replace(np.nan, avg_revenue, inplace=True)
# print(tesla_revenue.head())
tesla_revenue.sort_values(['Date'], ascending=True, axis=0, inplace=True)
tesla_revenue.set_index('Date', inplace=True)
tesla_revenue=tesla_revenue['Revenue'].astype('int')
# print(tesla_revenue.head())
tesla_revenue.plot(kind='line')
plt.title('Tesla Revenue 2010-2022 | TSLA')
plt.xlabel('Date')
plt.ylabel('Millions of US $')
plt.show()

