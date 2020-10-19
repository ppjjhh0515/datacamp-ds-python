'''
Replace multiple values II
As discussed in the video, instead of using the .replace() function multiple times to replace multiple values, you can use lists to map the elements you want to replace one to one with those you want to replace them with.

As you have seen in our popular names dataset, there are two names for the same ethnicity. We want to standardize the naming of each ethnicity by replacing

'ASIAN AND PACI' to 'ASIAN AND PACIFIC ISLANDER'
'BLACK NON HISP' to 'BLACK NON HISPANIC'
'WHITE NON HISP' to 'WHITE NON HISPANIC'
In the DataFrame names, you are going to replace all the values on the left by the values on the right.

Instructions
100 XP
Replace all the ethnicities by their respective alternative, as indicated above.
'''
start_time = time.time()

# Replace ethnicities as instructed
names['Ethnicity'].replace(['ASIAN AND PACI','BLACK NON HISP', 'WHITE NON HISP'], ['ASIAN AND PACIFIC ISLANDER','BLACK NON HISPANIC','WHITE NON HISPANIC'], inplace=True)

print("Time using .replace(): {} sec".format(time.time() - start_time))
