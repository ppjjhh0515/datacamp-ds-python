'''
Replace single values II
For this exercise, we will be using the names DataFrame. In this dataset, the column 'Rank' shows the ranking of each name by year. For this exercise, you will use dictionaries to replace the first ranked name of every year as 'FIRST', the second name as 'SECOND' and the third name as 'THIRD'.

You will use dictionaries to replace one single value per key.

You can already see the first 5 names of the data, which correspond to the 5 most popular names for all the females belonging to the 'ASIAN AND PACIFIC ISLANDER' ethnicity in 2011.

Instructions
100 XP
Replace the ranks, indicated in numbers, by strings, following the pattern given above. Don't hesitate to explore your dataset in the Console after replacing values to see how it changed.
'''
# Replace the number rank by a string
names['Rank'].replace({1:'FIRST', 2:'SECOND', 3:'THIRD'}, inplace=True)
print(names.head())
