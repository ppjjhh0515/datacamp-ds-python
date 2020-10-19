'''
Vectorization methods for looping a DataFrame
Now that you're familiar with vectorization in pandas and NumPy, you're going to compare their respective performances yourself.

Your task is to calculate the variance of all the hands in each hand using the vectorization over pandas Series and then modify your code using the vectorization over Numpy ndarrays method.
'''
# Calculate the variance in each hand
start_time = time.time()
poker_var = poker_hands[['R1', 'R2', 'R3', 'R4', 'R5']].var(axis=1)
print("Time using pandas vectorization: {} sec".format(time.time() - start_time))
print(poker_var.head())


# Calculate the variance in each hand
start_time = time.time()
poker_var = poker_hands[['R1', 'R2', 'R3','R4','R5']].values.var(axis=1, ddof=1)
print("Time using NumPy vectorization: {} sec".format(time.time() - start_time))
print(poker_var[0:5])
