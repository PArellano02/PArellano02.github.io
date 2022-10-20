# these are the term counts calculated in the lab
lab_dict = {'trump': 13924, 'russia': 412, 'obama': 2712, 'fake news': 333, 'mexico': 199}

# turn these folowings into lists 
terms = list(lab_dict.keys())
terms.sort()
accumulator = []
for term in terms:
    accumulator.append(lab_dict[term]) #looks for the key in the given term 

counts = accumulator

# the order of the keys is "nondeterministic" which basically means random
#order  in the order that the data appears like in the dictionary 
# Add order accordingly to analysis with the data
#The order we would l
# terms.sort()
# counts.sort()
# this code generates a plot
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(terms, counts)
plt.show()
