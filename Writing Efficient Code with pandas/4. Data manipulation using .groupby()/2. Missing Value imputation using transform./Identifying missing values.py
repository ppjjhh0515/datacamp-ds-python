'''
Identifying missing values
The first step before missing value imputation is to identify if there are missing values in our data, and if so, from which group they arise.

For the same restaurant_data data you encountered in the lesson, an employee erased by mistake the tips left in 65 tables. The question at stake is how many missing entries came from tables that smokers where present vs tables with no-smokers present.

Your task is to group both datasets according to the smoker variable, count the number or present values and then calculate the difference.

We're imputing tips to get you to practice the concepts taught in the lesson. From an ethical standpoint, you should not impute financial data in real life, as it could be considered fraud.

Instructions
100 XP
Group the data according to smoking status.
Calculate the number of non-missing values in each group.
Print the number of missing values in each group.
'''
# Group both objects according to smoke condition
restaurant_nan_grouped = restaurant_nan.groupby('smoker')

# Store the number of present values
restaurant_nan_nval = restaurant_nan_grouped['tip'].count()

# Print the group-wise missing entries
print(restaurant_nan_grouped['total_bill'].count() - restaurant_nan_nval)
