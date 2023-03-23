# Creating Dictionary:
Dictionary = {
    "Key": "Value",
    1: "Hello",
    2: "Welcome",
}

print("Dictionary-", Dictionary)  # printing Dictionary

# Changing values in Dictionary:
Dictionary[1] = "Value Changed" #
print("After changing value:", Dictionary)

# Adding keys and values in Dictionary:
Dictionary["New Key"] = "New Value"   #initialising key and value
print("After adding new key", Dictionary)

# Removing items from Dictionary:
Dictionary.pop("New Key")   # using pop function to remove item
print("Removing items", Dictionary)

# Nested Dictionary:
New_Dictionary = {1: True, 2: False}  # Creating new dictionary
Dictionary["New Dictionary"] = New_Dictionary  # Nesting new dictionary
print("Nested Dictionary", Dictionary)

# Updating Dictionary using update function:
Dictionary.update({1: "value updated"})  # updating value of key "1"
print("updated value: ", Dictionary)