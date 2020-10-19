'''
Validation of normalization
For this exercise, we will perform a z-score normalization and verify that it was performed correctly.

A distinct characteristic of normalized values is that they have a mean equal to zero and standard deviation equal to one.

After you apply the normalization transformation, you can group again on the same variable, and then check the mean and the standard deviation of each group.

You will apply the normalization transformation to every numeric variable in the poker_grouped dataset, which is the poker_hands dataset grouped by Class.

Instructions 1/2
50 XP
1
2
Apply the normalization transformation to the grouped object poker_grouped.
'''
zscore = lambda x: (x - x.mean()) / x.std()

# Apply the transformation
poker_trans = poker_grouped.transform(zscore)

# Re-group the grouped object and print each group's means and standard deviation
poker_regrouped = poker_trans.groupby(poker_hands['Class'])

print(np.round(poker_regrouped.mean(), 3))
print(poker_regrouped.std())
