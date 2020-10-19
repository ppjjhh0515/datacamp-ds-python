'''
.apply() function in every cell
As you saw in the lesson, you can use .apply() to map a function to every cell of the DataFrame, regardless the column or the row.

You're going to try it out on the poker_hands dataset. You will use .apply() to square every cell of the DataFrame. The native Python way to square a number n is n**2.

Instructions
100 XP
Define the lambda transformation for the square.
Apply the transformation using the .apply() function.
'''
# Define the lambda transformation
get_square = lambda x: x**2

# Apply the transformation
data_sum = poker_hands.apply(get_square)
print(data_sum.head())
