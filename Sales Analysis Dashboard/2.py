import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
file_path = r'C:\Users\CKS 36\Dropbox\My Coding Projects\Sales\cleaned_sales_data.csv'
data = pd.read_csv(file_path)

# Basic Analysis
# Total, Average, and Count of Sales by Product Line
product_line_stats = data.groupby('PRODUCTLINE').agg(Total_Sales=('SALES', 'sum'),
                                                     Average_Sales=('SALES', 'mean'),
                                                     Count=('SALES', 'count')).reset_index()

# Total Sales by Country
country_sales = data.groupby('COUNTRY').agg(Total_Sales=('SALES', 'sum')).reset_index()

# Sales Trends by Year
yearly_sales = data.groupby('YEAR_ID').agg(Total_Sales=('SALES', 'sum')).reset_index()

# Visualization with Matplotlib
plt.figure(figsize=(14, 7))

# Plot for Total Sales by Product Line
plt.subplot(1, 3, 1)
plt.bar(product_line_stats['PRODUCTLINE'], product_line_stats['Total_Sales'], color='blue')
plt.title('Total Sales by Product Line')
plt.xticks(rotation=45, ha='right')

# Plot for Total Sales by Country
plt.subplot(1, 3, 2)
plt.bar(country_sales['COUNTRY'], country_sales['Total_Sales'], color='green')
plt.title('Total Sales by Country')
plt.xticks(rotation=45, ha='right')

# Plot for Yearly Sales
plt.subplot(1, 3, 3)
plt.plot(yearly_sales['YEAR_ID'], yearly_sales['Total_Sales'], marker='o', linestyle='-')
plt.title('Yearly Sales Trends')
plt.xlabel('Year')
plt.ylabel('Total Sales')

plt.tight_layout()
plt.show()

# Save analysis results for Tableau
product_line_stats.to_csv(r'C:\Users\CKS 36\Dropbox\My Coding Projects\Sales\product_line_stats.csv', index=False)
country_sales.to_csv(r'C:\Users\CKS 36\Dropbox\My Coding Projects\Sales\country_sales.csv', index=False)
yearly_sales.to_csv(r'C:\Users\CKS 36\Dropbox\My Coding Projects\Sales\yearly_sales.csv', index=False)

print("Data analysis complete. Results saved for Tableau visualization.")
