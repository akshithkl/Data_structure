# 1. Create a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "Bangalore"
}
print("Initial Dictionary:", my_dict)

# 2. Add key-value pairs to the dictionary
my_dict["email"] = "alice@example.com"  # Adding new key-value pair
print("After Adding Email:", my_dict)

# 3. Remove key-value pairs from the dictionary
removed_value = my_dict.pop("age")  # Removes 'age' key
print("After Removing Age:", my_dict)
print("Removed Value:", removed_value)

# You can also completely delete the dictionary
del my_dict  # Deletes the dictionary entirely
# print(my_dict)  # This will give an error because the dictionary is deleted
