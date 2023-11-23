    #davaleba1
file_name = "user_information.txt"

with open(file_name, 'a') as file:
    while True:
        user_input = input("Enter information (type 'enough' to stop): ")
        
        if user_input.lower() == 'enough':
            break

        file.write(user_input + '\n')

print(f"THe information has been written to {file_name}")







    #davaleba2
import os

def create_folder_and_write_files():
    folder_name = input("Enter folder name: ")

    folder_path = os.path.join(os.getcwd(), folder_name)

    os.makedirs(folder_path, exist_ok=True)

    print(f"\nFolder '{folder_name}' created at {folder_path}")

    num_files = int(input("Enter the number of files to create: "))

    for i in range(1, num_files + 1):
        file_name = input(f"Enter name for file {i}: ")
        file_path = os.path.join(folder_path, file_name)

        file_content = input(f"Enter content for file {i}: ")

        with open(file_path, 'w') as file:
            file.write(file_content)

        print(f"File '{file_name}' created at {file_path} with content:\n{file_content}")

create_folder_and_write_files()














    #davaleba3
import os
from urllib.parse import quote

def text_to_morse(text):
    morse_code_dict = {'A': '.-', 'B': '-...','C': '-.-.', 'D': '-..', 'E': '.','F': '..-.', 'G': '--.', 
'H': '....','I': '..', 'J': '.---', 'K': '-.-','L': '.-..', 'M': '--', 'N': '-.',
'O': '---', 'P': '.--.', 'Q': '--.-','R': '.-.', 'S': '...', 'T': '-',
'U': '..-', 'V': '...-', 'W': '.--','X': '-..-', 'Y': '-.--', 'Z': '--..',
'0': '-----', '1': '.----', '2': '..---','3': '...--', '4': '....-', '5': '.....',
'6': '-....', '7': '--...', '8': '---..','9': '----.',
                       }

    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '

    return morse_code.strip()

def create_folder_and_write_morse_files():
    folder_name = input("Enter folder name: ")

    folder_path = os.path.join(os.getcwd(), folder_name)

    os.makedirs(folder_path, exist_ok=True)

    print(f"\nFolder '{folder_name}' created at {folder_path}")


    num_files = int(input("Enter the number of files to create: "))

    for i in range(1, num_files + 1):
        file_name = input(f"Enter name for file {i}: ")
        file_path = os.path.join(folder_path, file_name)

        file_content = input(f"Enter content for file {i}: ")

        with open(file_path, 'w') as file:
            file.write(file_content)

        morse_content = text_to_morse(file_content)

        with open(os.path.join(folder_path, f"{file_name}_morse.txt"), 'w') as morse_file:
            morse_file.write(morse_content)

        print(f"File '{file_name}' created at {file_path} with content:\n{file_content}")
        print(f"Morse code file '{file_name}_morse.txt' created with content:\n{morse_content}")


create_folder_and_write_morse_files()    



