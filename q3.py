#Task 1#
def update_dictionary(dct, key, value):
    if key in dct:
        print(f"The original value for '{key}' was: {dct[key]}")
    dct[key] = value
    
    return dct

#Task 2#
update_dictionary({}, "name", "Alice")
{'name': 'Alice'}

update_dictionary({"age": 25}, "age", 26)
The original value for 'age' was: 25
{'age': 26}
