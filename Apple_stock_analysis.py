import pandas as pd
import matplotlib.pyplot as plt
ap = pd.read_csv('apple.csv')
print(ap)
print('Максимальная цена акции ', ap.High.max())
print('Минимальная цена акции ', ap.Low.min())
len_apple = len(ap.index)
max_value = ap.Open[0]-ap.Close[0]
min_value = ap.Open[0]-ap.Close[0]
for i in range(len_apple):
    if(ap.Open[i] - ap.Close[i] >= max_value):
        max_value = ap.Open[i] - ap.Close[i]
    if(ap.Open[i] - ap.Close[i] <= min_value):
        min_value = ap.Open[i] - ap.Close[i]
print('Максимально положительная разница', max_value)
print('Максимально отрицательная разница', min_value)
ap = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)
ap = ap.sort_index()
print('Средняя цена открытия в 2015 году: ', ap.loc['2015', 'Open'].mean())
print('Средняя цена закрытия в 2015 году: ', ap.loc['2015', 'Close'].mean())
ap.loc['2012-Feb':'2017-Feb', ['Open']].plot()
plt.show()
