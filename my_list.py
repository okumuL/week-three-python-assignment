# my_list
my_list = []
# Append the following elements to my_list: 10, 20, 30, 40
my_list.extend([10, 20, 30, 40])
print(my_list)
# Output: [10, 20, 30, 40]

#Insert the value 15 at the second position in the list
my_list.insert(1, 15)
print(my_list)
# Output: [10, 15, 20, 30, 40]

#Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])
print(my_list)
# Output: [10, 15, 20, 30, 40, 50, 60, 70]

#Remove the last element from my_list
my_list.pop()
print(my_list)
# Output: [10, 15, 20, 30, 40, 50, 60]

#Sort my_list in ascending order
my_list.sort()
print(my_list)
# Output: [10, 15, 20, 30, 40, 50, 60]

#Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(index_of_30)
# Output: 3
