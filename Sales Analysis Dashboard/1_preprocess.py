import pandas as pd

file_path = r'C:\Users\CKS 36\Dropbox\My Coding Projects\Sales\sales_data_sample.csv'
clean_file_path = r'C:\Users\CKS 36\Dropbox\My Coding Projects\Sales\cleaned_sales_data.csv'

# Load the dataset
data = pd.read_csv(file_path, encoding='cp1252')

# Convert 'ORDERDATE' to datetime
data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'])

# Drop unnecessary columns
columns_to_drop = ['PHONE', 'ADDRESSLINE2']
data.drop(columns_to_drop, axis=1, inplace=True)

# Fill missing 'STATE' and 'TERRITORY' with 'Unknown', 'POSTALCODE' with the most common value
data['STATE'] = data['STATE'].fillna('Unknown')
data['TERRITORY'] = data['TERRITORY'].fillna('Unknown')
if data['POSTALCODE'].isnull().any():  # Only fill if there are nulls to avoid unnecessary computation
    most_common_postal = data['POSTALCODE'].mode()[0]
    data['POSTALCODE'] = data['POSTALCODE'].fillna(most_common_postal)

# Save the cleaned data to a new CSV file
data.to_csv(clean_file_path, index=False)

print("\nMissing values after handling:")
print(data.isnull().sum())
print("\nData cleaned and saved as 'cleaned_sales_data.csv'.")
