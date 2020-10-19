'''
Replace single values I
In this exercise, we will apply the following replacing technique of replacing multiple values using dictionaries on a different dataset.

We will apply the functions in the data DataFrame. Each row represents the rank of 5 cards from a playing card deck, spanning from 1 (Ace) to 13 (King) (features R1, R2, R3, R4, R5). The feature 'Class' classifies each row to a category (from 0 to 9) and the feature 'Explanation' gives a brief explanation of what each class represents.

The purpose of this exercise is to categorize the two types of flush in the game ('Royal flush' and 'Straight flush') under the 'Flush' name.

Instructions
100 XP
Replace every row of the DataFrame listed as 'Royal flush' or 'Straight flush' in the 'Explanation' column to 'Flush'.
'''
# Replace Royal flush or Straight flush to Flush
poker_hands.replace({'Royal flush':'Flush', 'Straight flush':'Flush'}, inplace=True)
print(poker_hands['Explanation'].head())
