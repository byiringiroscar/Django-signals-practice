test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 'oscar', 5]

# Printing original keys-value lists
print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))

# using naive method
# to convert lists to dictionary
res = {}
for key in test_keys:
    for value in test_values:
        res[key] = value
        test_values.remove(value)
        break

    # Printing resultant dictionary
print("Resultant dictionary is : " + str(res))








