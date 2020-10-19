'''
pandas vectorization in action
In this exercise, you will apply vectorization over pandas series to:

calculate the mean rank of all the cards in each hand (row)
calculate the mean rank of each of the 5 cards in each hand (column)
You will use the poker_hands dataset once again to compare both methods' efficiency.

Instructions
100 XP
Calculate the mean rank in each hand.
Calculate the mean rank of each of the 5 card in all hands.
'''
# Calculate the mean rank in each hand
row_start_time = time.time()
mean_r = poker_hands[['R1', 'R2', 'R3', 'R4', 'R5']].mean(axis=1)
print("Time using pandas vectorization for rows: {} sec".format(time.time() - row_start_time))
print(mean_r.head())

# Calculate the mean rank of each of the 5 card in all hands
col_start_time = time.time()
mean_c = poker_hands[['R1', 'R2', 'R3', 'R4', 'R5']].mean(axis=0)
print("Time using pandas vectorization for columns: {} sec".format(time.time() - col_start_time))
print(mean_c.head())
