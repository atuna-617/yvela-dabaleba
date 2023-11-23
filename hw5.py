    #davaleba1
consumer_info = []


for i in range(3):
    saxeli = input(f"შეიყვანეთ სახელი ნომერი {i + 1} მომხმარებლისთვის: ")
    gvari = input(f"შეიყყვანეთ გვარი ნომერი {i + 1} მომხმარებლისთვის: ")
    asaki = input(f"შეიყვანეთ ასაკი ნომერი {i + 1} მომხმარებლისთვის: ")
    
    user_info = [saxeli, gvari, asaki]
    
  
    consumer_info.append(user_info)

while True:
    try:
        user_index = int(input("შეიყვანეთ მომხარებლის ნომერი (1, 2, ან 3) რომ იხილოთ მათი ინფორმაცია: "))
        
        if 1 <= user_index <= 3:
            selected_user = consumer_info[user_index - 1]
            print("სახელი:", selected_user[0])
            print("გვარი:", selected_user[1])
            print("ასაკი:", selected_user[2])
        else:
            print("არასწორი ნომერი. გთხოვთ შეიყვანოთ 1, 2, ან 3.")
    except ValueError:
        print("ვხურავთ პროგრამას.")
        break
  






    #davaleba2
    user_data = []

def register_user():
    saxeli = input("Enter your name: ")
    paroli = input("Enter your password (8 characters or more): ")
    
    if saxeli != "" and len(paroli) >= 8:
        user_data.append({'name': saxeli, 'password': paroli})
        print("Registration successful!")
    else:
        print("Registration failed. Please provide a name and a password that containts at least 8 characters.")

def login():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    
    for user in user_data:
        if user['name'] == name and user['password'] == password:
            print("Login successful!")
            return
    print("Login failed. Invalid name or password.")

while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Select an option (1/2/3): ")
    
    if choice == '1':
        register_user()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")  
  
  
  
   
   
   
   
   
    #davaleba3
actors = [
    {
        'first_name': 'Ryan',
        'last_name': 'Gosling',
        'birth_year': 1980,
        'movies': ['Drive', 'Blade Runner 2049', 'Barbie.'],
    },
    {
        'first_name': 'Christian',
        'last_name': 'Bale',
        'birth_year': 1974,
        'movies': ['American Psycho', 'The Dark Knight', 'Ford v Ferrari.'],
    },
    {
        'first_name': 'Brad',
        'last_name': 'Pitt',
        'birth_year': 1963,
        'movies': ['Fight Club', 'Inglourious Basterds', 'Bullet Train.'],
    }
]


def find_actor(actor_name):
    for actor in actors:
        if actor['first_name'].lower() == actor_name.lower() or actor['last_name'].lower() == actor_name.lower():
            print(f"Actor: {actor['first_name']} {actor['last_name']}")
            print(f"Birth Year: {actor['birth_year']}")
            print("Famous Movies: " + ', '.join(actor['movies']))
            return

while True:
    actor_name = input("Enter the first or last name of a famous actor (or 'exit' to quit): ")
    
    if actor_name.lower() == 'exit':
        print("Exiting the program.")
        break
    else:
        find_actor(actor_name)



 
 
 
 
 
 
   