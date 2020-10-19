'''
apply() for rows iteration
.apply() is a very useful to iterate through the rows of a DataFrame and apply a specific function.

You will work on a subset of the poker_hands dataset, which includes only the rank of all the five cards of each hand in each row (this subset is generated for you in the script). You're going to get the variance of every hand for all ranks, and every rank for all hands.

Instructions 1/2
50 XP
1
Define a lambda function to return the variance, using the numpy package.
Apply the transformation for every row.
'''

get_variance = lambda x: np.var(x)

# Apply the transformation every rows
data_tr = poker_hands[['R1', 'R2', 'R3', 'R4', 'R5']].apply(get_variance, axis=1)
print(data_tr.head())

get_variance = lambda x: np.var(x)

# Apply the transformation every columns
data_tr = poker_hands[['R1', 'R2', 'R3', 'R4', 'R5']].apply(get_variance, axis=0)
print(data_tr.head())
