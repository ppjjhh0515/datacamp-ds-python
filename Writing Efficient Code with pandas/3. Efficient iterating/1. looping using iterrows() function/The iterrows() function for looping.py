'''
The iterrows() function for looping
You just saw how to create a generator out of a pandas DataFrame. You will now use this generator and see how to take advantage of that method of looping through a pandas DataFrame, still using the poker_hands dataset.

Specifically, we want the sum of the ranks of all the cards, if the index of the hand is an odd number. The ranks of the cards are located in the odd columns of the DataFrame.

Instructions
100 XP
Check if the hand index is an odd number.
If it is, calculate the sum of the rank of all the cards in that hand. It could take a little longer than usual to compute the results.
'''
data_generator = poker_hands.iterrows()

for index, values in data_generator:
  	# Check if index is odd
    if index % 2 == 1:
      	# Sum the ranks of all the cards
        hand_sum = sum([values[1], values[3], values[5], values[7], values[9]])
