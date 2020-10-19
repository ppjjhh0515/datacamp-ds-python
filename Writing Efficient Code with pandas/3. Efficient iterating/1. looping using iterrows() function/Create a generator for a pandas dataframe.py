'''
Create a generator for a pandas DataFrame
As you've seen in the video, you can easily create a generator out of a pandas DataFrame. Each time you iterate through it, it will yield two elements:

the index of the respective row
a pandas Series with all the elements of that row
You are going to create a generator over the poker dataset, imported as poker_hands. Then, you will print all the elements of the 2nd row, using the generator.

Remember you can always explore the dataset and see how it changes in the IPython Shell, and refer to the slides in the Slides tab.

Instructions
100 XP
Assign a generator over the rows of the data dataset on the variable generator.
Print all the elements of the 2nd element of the created generator.
'''
# Create a generator over the rows
generator = poker_hands.iterrows()

# Access the elements of the 2nd row
first_element = next(generator)
second_element = next(generator)
print(first_element, second_element)
