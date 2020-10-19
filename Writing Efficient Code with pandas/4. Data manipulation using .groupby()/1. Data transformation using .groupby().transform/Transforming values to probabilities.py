'''
Transforming values to probabilities
In this exercise, we will apply a probability distribution function to a pandas DataFrame with group related parameters by transforming the tip variable to probabilities.

The transformation will be a exponential transformation. The exponential distribution is defined as

e−λ∗x∗λ
where λ (lambda) is the mean of the group that the observation x belongs to.

You're going to apply the exponential distribution transformation to the size of each table in the dataset, after grouping the data according to the time of the day the meal took place. Remember to use each group's mean for the value of λ.

In Python, you can use the exponential as np.exp() from the NumPy library and the mean value as .mean().

Instructions
100 XP
Define the exponential distribution transformation exp_tr.
Group the data according to the time the meal took place.
Apply the transformation to the grouped data.
'''
# Define the exponential transformation
exp_tr = lambda x: np.exp(-x.mean()*x) * x.mean()

# Group the data according to the time
restaurant_grouped = restaurant_data.groupby('time')

# Apply the transformation
restaurant_exp_group = restaurant_grouped['tip'].transform(exp_tr)
print(restaurant_exp_group.head())
