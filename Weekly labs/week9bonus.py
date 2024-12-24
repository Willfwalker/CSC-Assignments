import pandas as pd
import matplotlib.pyplot as plt
# Load data
df = pd.read_csv("./data/sales_data.csv")
print(df)
# Calculate total sales
total_sales = df['sales'].sum()
print(f"Total Sales: ${total_sales}")
# Visualization
df.plot(kind='bar', x='product', y='sales')
plt.title("Sales Data")
plt.ylabel("Sales in USD")
plt.show()
