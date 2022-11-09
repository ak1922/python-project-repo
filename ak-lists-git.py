# # create a variable fruit with a list of fruits
# fruits = ['apple', 'banana', 'orange']
# print(fruits)
# print(len(fruits))  # check how many items are in fruits
# print()

# fruits.append('grapes') # add grapes to the list of fruits
# print(fruits)
# print(len(fruits))  # check how many items are in fruits
# print()

# fruits.insert(2, 'lemon')   # add 
# print(fruits)
# print(len(fruits))  # check how many items are in fruits
# print()

# print(type(fruits))     # check data type for fruits
# fruits_tuple = tuple(fruits)    # convert fruits to a tuple
# print(fruits_tuple)
# print(type(fruits_tuple))   # check data type fruits_tuple
# print()

# print(fruits)
# fruits_sort = fruits.sort(reverse=False)    # sort fruits decending
# print(fruits)
# print()

# print(fruits)
# fruits_sort = fruits.sort(reverse=True) # sort fruits ascending
# print(fruits)
# print()

# print(fruits)
# print(fruits[0])
# print(fruits[4])

# variable list of verbs
rse = ['make', 'take', 'run', 'taste', 'eat', 'walk', 'climb', 'drive', 'wade']
print(rse)
print()

# get index on rse with enumerate
rse_idx = enumerate(rse)
print(list(rse_idx))

rse[-1] = ['call']  # change the last word to call
print(rse)

rse.pop(-1) # remove last verb from list
print(rse)
print()

rse.append('call')  # add call to end of list
print(rse)

rse[-1] = 'break'   # change last work to break
print(rse)

# create new variable with list of names
cac = ['Max', 'Tom', 'Angela', 'May', 'Andrea']
rse.extend(cac)     # use extend to add cac list to rse list
print(rse)
rse_idx = enumerate(rse)
print(list(rse_idx))
