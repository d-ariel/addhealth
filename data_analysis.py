import pandas
import numpy

#Read in data set
my_addHealth = pandas.read_csv('addhealth_pds.csv')

print(len(my_addHealth)) #number of observations (rows)
print(len(my_addHealth.columns)) #number of variables (columns)

print("counts for H1RP1 - How much do you feel that adults care about you?")
c1 = my_addHealth["H1PR1"].value_counts(sort=True)
print(c1)

print("percentage for H1RP1 - How much do you feel that adults care about you?")
p1 = my_addHealth["H1PR1"].value_counts(sort=True, normalize=True)
print(p1)
