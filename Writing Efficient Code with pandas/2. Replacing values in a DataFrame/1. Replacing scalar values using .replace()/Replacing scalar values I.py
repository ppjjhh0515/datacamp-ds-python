'''
Replacing scalar values I
In this exercise, we will replace a list of values in our dataset by using the .replace() method with another list of desired values.

We will apply the functions in the poker_hands DataFrame. Remember that in the poker_hands DataFrame, each row of columns R1 to R5 represents the rank of each card from a player's poker hand spanning from 1 (Ace) to 13 (King). The Class feature classifies each hand as a category, and the Explanation feature briefly explains each hand.

The poker_hands DataFrame is already loaded for you, and you can explore the features Class and Explanation.

Remember you can always explore the dataset and see how it changes in the IPython Shell, and refer to the slides in the Slides tab.

Instructions
100 XP
Replace every hand (row) of the DataFrame listed as Class 1 (One Pair) to -2 and each hand listed as Class 2 (Two Pairs) to -3.
'''
# Replace Class 1 to -2 
poker_hands['Class'].replace(1, -2, inplace=True)
# Replace Class 2 to -3
poker_hands['Class'].replace(2, -3, inplace=True)

print(poker_hands[['Class', 'Explanation']])
