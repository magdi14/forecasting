from datetime import datetime

import pandas as pd


def load_excel():
    df = pd.read_excel('dataset.xls')
    df = df[(df['Category'] == 'Furniture') | (df['Category'] == 'Office Supplies')][['Order Date', 'Sales']]
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    df['Date'] = [datetime(i, j, 1) for (i, j) in zip(df['Year'], df['Month'])]
    df = df[['Date', 'Sales']].groupby(df['Date']).sum()
    return df


