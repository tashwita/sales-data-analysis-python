import pandas as pd

df = pd.read_csv("ecommerce_sales.csv")
print(df.columns)
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

import matplotlib.pyplot as plt
import seaborn as sns
df.columns = df.columns.str.strip()

df['Month'] = df['Order Date'].dt.month
df.columns = df.columns.str.strip()

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

category_sales = df.groupby('Category')['Sales'].sum()
print("\nSales by Category:\n", category_sales)

region_sales = df.groupby('Region')['Sales'].sum()
print("\n Sales by Region:\n" , region_sales)

monthly_sales = df.groupby('Month')['Sales'].sum()
print("\nmonthly sales:\n", monthly_sales)

category_sales.plot(kind='bar', title="Sales by Category")
plt.show()

monthly_sales.plot(title="Monthly sales trend")
plt.show()

region_sales.plot(kind='pie', autopct='%1.1f%%', title="Region Share")
plt.show()

sns.barplot(x='Category', y='Profit',data=df)
plt.title("profit by category")
plt.show()
