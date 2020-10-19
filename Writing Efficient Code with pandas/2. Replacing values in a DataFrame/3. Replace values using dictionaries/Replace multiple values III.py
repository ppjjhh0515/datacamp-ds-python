'''
Replace multiple values III
As you saw in the video, you can use dictionaries to replace multiple values with just one value, even from multiple columns. To show the usefulness of replacing with dictionaries, you will use the names dataset one more time.

In this dataset, the column 'Rank' shows which rank each name reached every year. You will change the rank of the first three ranked names of every year to 'MEDAL' and those from 4th and 5th place to 'ALMOST MEDAL'.

You can already see the first 5 names of the data, which correspond to the 5 most popular names for all the females belonging to the 'ASIAN AND PACIFIC ISLANDER' ethnicity in 2011.

Instructions
100 XP
Replace the first three ranked names of every year to 'MEDAL'.
Replace the fourth and fifth ranked names of every year to 'ALMOST MEDAL'.
'''

# Replace the rank of the first three ranked names to 'MEDAL'
names.replace({'Rank': {1:'MEDAL', 2:'MEDAL', 3:'MEDAL'}}, inplace=True)

# Replace the rank of the 4th and 5th ranked names to 'ALMOST MEDAL'
names.replace({'Rank': {4:'ALMOST MEDAL', 5:'ALMOST MEDAL'}}, inplace=True)
print(names.head())
