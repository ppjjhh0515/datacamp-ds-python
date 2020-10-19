'''
The min-max normalization using .transform()
A very common operation is the min-max normalization. It consists in rescaling our value of interest by deducting the minimum value and dividing the result by the difference between the maximum and the minimum value. For example, to rescale student's weight data spanning from 160 pounds to 200 pounds, you subtract 160 from each student's weight and divide the result by 40 (200 - 160).

You're going to define and apply the min-max normalization to all the numerical variables in the restaurant data. You will first group the entries by the time the meal took place (Lunch or Dinner) and then apply the normalization to each group separately.

Remember you can always explore the dataset and see how it changes in the IPython Shell, and refer to the slides in the Slides tab.

Instructions
100 XP
Define the min-max normalization using the lambda method.
Group the data according to the time the meal took place.
Apply the transformation to the grouped data.
'''

# Define the min-max transformation
min_max_tr = lambda x: (x - x.min()) / (x.max() - x.min())

# Group the data according to the time
restaurant_grouped = restaurant_data.groupby('time')

# Apply the transformation
restaurant_min_max_group = restaurant_grouped.transform(min_max_tr)
print(restaurant_min_max_group.head())
