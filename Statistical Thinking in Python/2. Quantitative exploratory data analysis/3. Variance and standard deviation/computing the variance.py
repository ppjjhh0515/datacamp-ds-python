'''
Computing the variance
It is important to have some understanding of what commonly-used functions are doing under the hood. Though you may already know how to compute variances, this is a beginner course that does not assume so. In this exercise, we will explicitly compute the variance of the petal length of Iris veriscolor using the equations discussed in the videos. We will then use np.var() to compute it.

Instructions
100 XP
Create an array called differences that is the difference between the petal lengths (versicolor_petal_length) and the mean petal length. The variable versicolor_petal_length is already in your namespace as a NumPy array so you can take advantage of NumPy's vectorized operations.
Square each element in this array. For example, x**2 squares each element in the array x. Store the result as diff_sq.
Compute the mean of the elements in diff_sq using np.mean(). Store the result as variance_explicit.
Compute the variance of versicolor_petal_length using np.var(). Store the result as variance_np.
Print both variance_explicit and variance_np in one print call to make sure they are consistent.
'''
# Array of differences to mean: differences
differences = (versicolor_petal_length - versicolor_petal_length.mean())

# Square the differences: diff_sq
diff_sq = differences ** 2

# Compute the mean square difference: variance_explicit
variance_explicit = diff_sq.mean()

# Compute the variance using NumPy: variance_np
variance_np = versicolor_petal_length.var()

# Print the results
print(variance_explicit, variance_np)


