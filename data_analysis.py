import pandas
import numpy

#read in data set
my_addHealth = pandas.read_csv('addhealth_pds.csv', low_memory=False)

#upper-case all My Health dataframe column names
my_addHealth.columns = map(str.upper, my_addHealth.columns)

pandas.set_option('display.float_format', lambda x:'%f'%x)

#convert relevant output objects to numeric
my_addHealth["H1PR1"] = pandas.to_numeric(my_addHealth["H1PR1"])
my_addHealth["H1PR2"] = pandas.to_numeric(my_addHealth["H1PR2"])
my_addHealth["H1PR3"] = pandas.to_numeric(my_addHealth["H1PR3"])
my_addHealth["H1EE1"] = pandas.to_numeric(my_addHealth["H1EE1"])
my_addHealth["H1EE2"] = pandas.to_numeric(my_addHealth["H1EE2"])

# var H1EE1 represents adolescents' self-reported desires to go to college (measured on a scale of 1-5).
# var H1EE2 represents adolescents' self-reported likelihood of attending college (measured on a scale of 1-5).
# this creates a subset of the initial dataframe that is limited to
# responses with H1EE1 = 5 (very likely) and H1EE2 = 5 (very likely).

my_addHealth_subset = my_addHealth[(my_addHealth["H1EE1"] == 5) & (my_addHealth["H1EE2"] == 5)] #subset
my_addHealth_subset_copy = my_addHealth_subset.copy() #copy of subset

# to demonstrate that my subset is populated correctly:
print("The number of observations in H1EE1 should be equivalent to the number of observations in H1EE2.")
print(my_addHealth_subset_copy["H1EE1"].value_counts(sort=True)) #contains only entries containing H1EE1 = 5
print(my_addHealth_subset_copy["H1EE2"].value_counts(sort=True)) #contains only entries containing H1EE2 = 5

#frequency distributions for 3 variables related to perceived care from adults, teachers, and parents
print("distribution for variable H1PR1 - How much do you feel that adults care about you?")
adults_care = my_addHealth_subset_copy["H1PR1"].value_counts(sort=True)
print(adults_care)

print("distribution for variable H1PR2 - How much do you feel that your teachers care about you?")
teachers_care = my_addHealth_subset_copy["H1PR2"].value_counts(sort=True)
print(teachers_care)

print("distribution for variable H1PR3 - How much do you feel that your parents care about you?")
parents_care = my_addHealth_subset_copy["H1PR3"].value_counts(sort=True)
print(parents_care)
