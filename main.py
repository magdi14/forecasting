from load import load
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
from metrics import mse, mape, lad
from tabulate import tabulate

data = load()
data['Moving Average'] = data['Sales'].rolling(window=4).mean()
data['α=0.1'] = data['Sales'].ewm(alpha=0.1, adjust=False).mean()
data['α=0.5'] = data['Sales'].ewm(alpha=0.5, adjust=False).mean()

print(tabulate(data, headers=["Date", "Sales", "Moving Average", "α=0.1", "α=0.5"], tablefmt='fancy_grid',
               floatfmt='.4f'))

sales = data['Sales']
elements = seasonal_decompose(sales, model='multiplicative')
data.plot()
elements.plot()
plt.show()

print(tabulate([["MSE", mse(data['Sales'].iloc[3:], data['Moving Average'].iloc[3:]), mse(data['Sales'], data['α=0.1']),
                 mse(data['Sales'], data['α=0.5'])],
                ["MAPE", mape(data['Sales'].iloc[3:], data['Moving Average'].iloc[3:]),
                 mape(data['Sales'], data['α=0.1']),
                 mape(data['Sales'], data['α=0.5'])],
                ["LAD", lad(data['Sales'].iloc[3:], data['Moving Average'].iloc[3:]), lad(data['Sales'], data['α=0.1']),
                 lad(data['Sales'], data['α=0.5'])]], headers=["Moving Average", "α=0.1", "α=0.5"],
               tablefmt='fancy_grid', floatfmt='.2f'))
