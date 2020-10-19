'''
Data filtration
As you noticed in the video lesson, you may need to filter your data for various reasons.

In this exercise, you will use filtering to select a specific part of our DataFrame:

by the number of entries recorded in each day of the week
by the mean amount of money the customers paid to the restaurant each day of the week
Instructions 1/3
35 XP
1
2
3
Create a new DataFrame containing only the days when the count of total_bill is greater than 40.
'''
# Filter the days where the count of total_bill is greater than $40
total_bill_40 = restaurant_data.groupby('day').filter(lambda x: x['total_bill'].count() > 40)

# Print the number of tables where total_bill is greater than $40
print('Number of tables where total_bill is greater than $40:', total_bill_40.shape[0])

'''
From the total_bill_40 DataFrame, select only the entries that have a mean total_bill greater than $20, grouped by day.

'''
# Filter the days where the count of total_bill is greater than $40
total_bill_40 = restaurant_data.groupby('day').filter(lambda x: x['total_bill'].count() > 40)

# Select only the entries that have a mean total_bill greater than $20
total_bill_20 = total_bill_40.groupby('day').filter(lambda x : x['total_bill'].mean() > 20)

# Print days of the week that have a mean total_bill greater than $20
print('Days of the week that have a mean total_bill greater than $20:', total_bill_20.day.unique())

