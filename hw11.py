    #davaleba1
def unique_list(input_list):
    unique_elements = list(set(input_list))
    return unique_elements

input_list = [1, 2, 2, 3, 4, 4, 5]
result_list = unique_list(input_list)
print(result_list)  







    #davaleba2
def immutable_set(input_list):
    unique_elements = frozenset(input_list)
    return unique_elements

input_list = [1, 2, 2, 3, 4, 4, 5]
result_frozenset = immutable_set(input_list)
print(result_frozenset)  







    #davaleba3
def set_to_tuple(set1, set2):
    combined_set = set1.union(set2)
    result_tuple = tuple(combined_set)
    return result_tuple

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result_tuple = set_to_tuple(set1, set2)
print(result_tuple) 





    
    #davaleba4
def hash_password(password):
    return password  

def user_info():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    hashed_password = hash_password(password)

    user_data = (username, hashed_password)

    user_list.append(user_data)
    return user_list


user_list = []

user_info()
print(user_list)  
