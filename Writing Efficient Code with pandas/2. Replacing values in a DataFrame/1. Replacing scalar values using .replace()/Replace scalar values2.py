'''
Replace scalar values II
As discussed in the video, in a pandas DataFrame, it is possible to replace values in a very intuitive way: we locate the position (row and column) in the Dataframe and assign in the new value you want to replace with. In a more pandas-ian way, the .replace() function is available that performs the same task.

You will be using the names DataFrame which includes, among others, the most popular names in the US by year, gender and ethnicity.

Your task is to replace all the babies that are classified as FEMALE to GIRL using the following methods:

intuitive scalar replacement
using the .replace() function
Instructions 1/3
35 XP
1
2
3
Replace all the babies that are classified as 'FEMALE' to 'GIRL' as described above.
'''
start_time = time.time()

# Replace all the entries that has 'FEMALE' as a gender with 'GIRL'
names['Gender'].loc[names.Gender == 'FEMALE'] = 'GIRL'

print("Time using .loc[]: {} sec".format(time.time() - start_time))


# 2nd problem
start_time = time.time()

# Replace all the entries that has 'FEMALE' as a gender with 'GIRL'
names['Gender'].replace('FEMALE', 'GIRL', inplace=True)

print("Time using .replace(): {} sec".format(time.time() - start_time))
