    #davaleba1
def remove_duplicates_(dictionary):
    unique_values = list(set(dictionary.values()))
    unique_dict = {key: value for key, value in dictionary.items() if value in unique_values}
    return unique_dict

my_dict = {
    'a': 1, 'b': 2, 'a': 1, 'd': 3, 'e': 2
}

result = remove_duplicates_(my_dict)
print("Original Dictionary:", my_dict)
print("Dictionary with Unique Values:", result)







    #davaleba2
def is_dict_empty(my_dict):
    if not my_dict:
        return True
    else:
        return False

empty_dict = {}
full_dict = {'a': 1, 'b': 2}

print("Is the empty_dict empty?", is_dict_empty(empty_dict))
print("Is the non_empty_dict empty?", is_dict_empty(full_dict))








    #davaleba3
def create_letter_count_dict(input_string):
    letter_count = {}
    for letter in input_string:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count


sample_string = 'w3schools'

result_dict = create_letter_count_dict(sample_string)
print("Dictionary with letter counts:", result_dict)











    #davaleba4
def get_key_value_items(my_dict):
    print("Keys:")
    for key in my_dict:
        print(key)

    print("\nValues:")
    for value in my_dict.values():
        print(value)

    print("Items:")
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")


sample_dict = {'a': 1, 'b': 2, 'c': 3}

get_key_value_items(sample_dict)
