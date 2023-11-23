    #დავალება1
#user_input = input("შეიყვანეთ წინადადება: ")
#
#num_letters = 0
#num_numbers = 0
#num_symbols = 0
#
#for char in user_input:
#    if char.isalpha():
#        num_letters += 1
#    elif char.isdigit():
#        num_numbers += 1
#    else:
#        num_symbols += 1
#
#print(f"ასოთა რაოდენობა: {num_letters}")
#print(f"რიცხვთა რაოდენობა: {num_numbers}")
#print(f"სიმბოლოთა რაოდენობა: {num_symbols}")
 

   #დავალება2
#sentence1 = input("შეიყვანეთ პირველი წინადადება: ")
#sentence2 = input("შეიყვანეთ მეორე წინადადება: ")
#
#if len(sentence1) > 0 and len(sentence2) > 0:
#    new_sentence = sentence1[0] + sentence2[-1] + sentence1[1] + sentence2[-1]
#    print("შედგენილი წინადადება:", new_sentence)

    #დავალება3
winadadeba1 = input("შეიყვანეთ პირველი წინადადება: ")
winadadeba2 = input("შეიყვანეთ მეორე წინადადება: ")

def are_strings_balanced(str1, str2):
    for char in str1:
        if char not in str2:
            return False

    for char in str2:
        if char not in str1:
            return False

    return True

if are_strings_balanced(winadadeba1, winadadeba2):
    print("Strings are balanced!")
else:
    print("Strings are not balanced!")
