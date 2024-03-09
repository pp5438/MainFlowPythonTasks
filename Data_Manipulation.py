# Create a list
my_list = [1, 2, 3, 4, 5]

# Adding elements to the list
my_list.append(6)

# Removing an element from the list
my_list.remove(3)

# Modifying an element in the list
my_list[0] = 10

print("List:", my_list)

# Create a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}

# Adding a key-value pair to the dictionary
my_dict["d"] = 4

# Removing a key-value pair from the dictionary
del my_dict["b"]

# Modifying a value in the dictionary
my_dict["a"] = 100

print("Dictionary:", my_dict)

# Create a set
my_set = {1, 2, 3, 4, 5}

# Adding an element to the set
my_set.add(6)

# Removing an element from the set
my_set.remove(3) if 3 in my_set else None

print("Set:", my_set)
