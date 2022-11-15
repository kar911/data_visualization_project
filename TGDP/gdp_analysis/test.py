 import matplotlib.pyplot as plt,
 import pandas as pd

 plt.style.use('bmh')
 df = pd.read_csv('country-codes.csv')

 x = df['code']
 y = df['name']

 plt.xlabel('code', fontsize=18)
 plt.ylabel('name',fontsize=16)
 plt.bar(x,y)
 plt.plot()

 plt.Show()