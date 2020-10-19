'''
Missing value imputation
As the majority of the real world data contain missing entries, replacing these entries with sensible values can increase the insight you can get from our data.

In the restaurant dataset, the "total_bill" column has some missing entries, meaning that you have not recorded how much some tables have paid. Your task in this exercise is to replace the missing entries with the median value of the amount paid, according to whether the entry was recorded on lunch or dinner (time variable).

Instructions 1/2
50 XP
1
2
Define the lambda function that fills missing values with the median.
Apply and print the pre-defined transformation to impute the missing values in the restaurant_data dataset.
'''
# Define the lambda function
missing_trans = lambda x: x.fillna(x.median())

# Group the data according to time
restaurant_grouped = restaurant_data.groupby('time')

# Apply the transformation
restaurant_impute = restaurant_grouped.transform(missing_trans)
print(restaurant_impute.head())
