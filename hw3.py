    #davaleba1
#import random
#
#def get_user_choice():
#    while True:
#        user_choice = input("შეიყვანეთ თქვენი არჩევანი (ქვა/ფურცელი/მაკრატელი): ").strip().capitalize()
#        if user_choice in ["ქვა", "ფურცელი", "მაკრატელი"]:
#            return user_choice
#        else:
#            print("არასწორი არჩევანი. გთხოვთ აირჩიოთ ქვა, ფურცელი, ან მაკრატელი.")
#
#def get_computer_choice():
#    return random.choice(["ქვა", "ფურცელი", "მაკტარელი"])
#
#def determine_winner(user_choice, computer_choice):
#    if user_choice == computer_choice:
#        return "ფრე არის !"
#    elif (
#        (user_choice == "ქვა" and computer_choice == "მაკრატელი") or
#        (user_choice == "ფურცელი" and computer_choice == "ქვა") or
#        (user_choice == "მაკრატელი" and computer_choice == "ფურცელი")
#    ):
#        return "თქვენ გაიმარჯვეთ!"
#    else:
#        return "კომპიუტერმა მოიგო!"
#
#def main():
#    user_wins = 0
#    computer_wins = 0
#
#    while user_wins < 3 and computer_wins < 3:
#        user_choice = get_user_choice()
#        computer_choice = get_computer_choice()
#        print(f"თქვენ აირჩიეთ {user_choice}, კომპუტერმა აირჩია {computer_choice}")
#        
#        result = determine_winner(user_choice, computer_choice)
#        print(result)
#        
#        if result == "თქვენ გაიმარჯვეთ!":
#            user_wins += 1
#        elif result == "კომპიუტერმა გაიმარჯვა!":
#            computer_wins += 1
#
#    if user_wins > computer_wins:
#        print("გილოცავთ! თამაში მოიგეთ")
#    else:
#        print("კომპიუტერმა მოიგო თამაში!")
#
#if __name__ == "__main__":
#    main()


    #დავალება2
#try:
#    num = int(input("შეიყვანეთ რიცხვი: "))
#    
#    if num < 1:
#        print("შეიყვანეთ დადებით რიცხვი.")
#    else:
#        print(f"გამრავლების ტაბულა 1-დან {num}-მდე:")
#
#        for i in range(1, num + 1):
#            for j in range(1, num + 1):
#                result = i * j
#                print(f"{i} x {j} = {result}\t", end="")
#            print() 
#except ValueError:
#    print("არასწორი ინპუტი.")

    #დაველბა3
#
#account_balance = 3000
#
#while True:
#    try:
#        danaxarji = float(input("ფასი (ან 0 რომ გაჩერდეს): GEL "))
#        
#        if danaxarji < 0:
#            print("შეიყვანეთ რაოდენობა.")
#        elif danaxarji == 0:
#            break  
#        elif danaxarji > account_balance:
#            print("არ არის საკმარისი თანხა.")
#        else:
#            account_balance -= danaxarji
#            print(f"დარჩენილი ბალანსი: {account_balance} GEL")
#    except ValueError:
#        print("შეცდომა.")
#
    #დავალება4
#while True:
#    user_input = input("შეიყვანეთ რაც გინდათ (ან დაწერეთ 'გასვლა' რომ დატოვოთ თამაში): ")
#    
#    if user_input.lower() == "გასვლა":
#        break
#    
#    print("User Said Whaaat!?")
#    print(f"User Said {user_input}")
