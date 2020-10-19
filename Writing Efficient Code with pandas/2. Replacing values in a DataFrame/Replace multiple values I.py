'''
Replace multiple values I
In this exercise, you will apply the .replace() function for the task of replacing multiple values with one or more values. You will again use the names dataset which contains, among others, the most popular names in the US by year, gender and Ethnicity.

Thus you want to replace all ethnicities classified as black or white non-hispanics to non-hispanic. Remember, the ethnicities are stated in the dataset as follows: ['BLACK NON HISP', 'BLACK NON HISPANIC', 'WHITE NON HISP' , 'WHITE NON HISPANIC'] and should be replaced to 'NON HISPANIC'

Instructions 1/2
50 XP
1
Replace all the ethnicities that are not Hispanic in the dataset to 'NON HISPANIC' using the.loc()` indexer.
'''
start_time = time.time()

# Replace all non-Hispanic ethnicities with 'NON HISPANIC'
names['Ethnicity'].loc[(names["Ethnicity"] == 'BLACK NON HISP') | 
                      (names["Ethnicity"] == 'BLACK NON HISPANIC') | 
                      (names["Ethnicity"] == 'WHITE NON HISP') | 
                      (names["Ethnicity"] == 'WHITE NON HISPANIC')] = "NON HISPANIC"

print("Time using .loc[]: sec".format(time.time() - start_time))



start_time = time.time()

# Replace all non-Hispanic ethnicities with 'NON HISPANIC'
names['Ethnicity'].replace(['BLACK NON HISP', 'BLACK NON HISPANIC', 'WHITE NON HISP' , 'WHITE NON HISPANIC'], 'NON HISPANIC', inplace=True)

print("Time using .replace(): {} sec".format(time.time() - start_time))
