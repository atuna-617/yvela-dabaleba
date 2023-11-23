    #davaleba 1
#question = "რომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც?”"
#answers = {
#    1: "შუმერთა ",
#    2: "სელჩუკთა ",
#    3: "რომის ",
#    4: "მონღოლთა"
#}
#
#correct_answer = 3
#
#print(question)
#for num, ans in answers.items():
#    print(f"{num}. {ans}")
#
#user_input = input("შეიყვანეთ სწორი პასუხის ნომერი ან თავად სწორი პასუხი:")
#
#if user_input.isdigit():
#    user_input = int(user_input)
#    if user_input == correct_answer:
#        print("სწორია!")
#    else:
#        print(f"არა! სწორი პასუხია {answers[correct_answer]}!")
#elif user_input.capitalize() == answers[correct_answer]:
#    print("სწორია!")
#else:
#    print(f"არა! სწორი პასუხია {answers[correct_answer]}!")

#
#    #davaleba 2
#product_categories = {
#    "ლეპტოპლები": ["ლეპტოპი A", "ლეპტოპი B", "ლეპტოპი C", "ლეპტოპი D"],
#    "კომპიუტერები": ["კომპიუტერი A", "კომპიუტერი B", "კომპიუტერი C", "კომპიუტერი D"],
#    "ტელეფონები": ["ტელეფონი A", "ტელეფონი B", "ტელეფონი C", "ტელეფონი D"],
#}
#
#product_prices = {
#    "ლეპროპი A": 1000,
#    "ლეპროპი B": 1200,
#    "ლეპროპი C": 800,
#    "ლეპროპი D": 1500,
#    "კომპიუტერი A": 600,
#    "კომპიუტერი B": 800,
#    "კომპიუტერი C": 700,
#    "კომპიუტერი D": 900,
#    "ტელეფონი A": 300,
#    "ტელეფონი B": 400,
#    "ტელეფონი C": 250,
#    "ტელეფონი D": 500,
#}
#
#
#print("ამოირჩიეთ პროდუქტის კატეგორია:")
#for i, category in enumerate(product_categories.keys(), start=1):
#    print(f"{i}. {category}")
#
#category_choice = input("შეიყვანეთ თქვენი სასურველი კატეგორიის რიცხვი : ") 
#
#if category_choice.isdigit() and 1 <= int(category_choice) <= len(product_categories):
#    category_choice = list(product_categories.keys())[int(category_choice) - 1]
#    max_budget = float(input(f"თქვენი ბიუჯეტი {category_choice}სთვის: "))
#
#    matching_products = [
#        product
#        for product in product_categories[category_choice]
#        if product_prices[product] <= max_budget
#    ]
#
#    if matching_products:
#        print(f"ხელმისაწვდომია {category_choice}:")
#        for product in matching_products:
#            print(f"- {product} (ფასი: ${product_prices[product]})")
#    else:
#        print(f"არ არის ხელმისაწვდომი {category_choice}.")
#else:
#    print("არასწორი კატეგორიის არჩევანი.")


    #davaleba
#fuelconsumption_per_km = 12
#
#mandzili = {
#    "ზარაგოზა": 50,
#    "ვალენსია": 75,
#    "მადრიდი": 100,
#}
#
#sawvavi = float(input("შეიყვანეთ დარჩენილი საწვავი (ლიტრებში): "))
#
#max_distance = sawvavi / fuelconsumption_per_km
#
#reachable_cities = []
#
#
#for city, distance in mandzili.items():
#    if distance <= max_distance:
#        reachable_cities.append(city)
#
#if reachable_cities:
#    print("ქალაქები რომელბშიც შეგიძლიათ დაჯდომა:")
#    for city in reachable_cities:
#        print(city)
#else:
#    print("!ავარიული დაშვება!")

  

    #davaleba 4

#def kitxva(kitxva):
#    response = input(kitxva + " (დიახ/არა): ").strip().lower()
#    while response not in ["დიახ", "არა"]:
#        print("შეიყვანეთ 'დიახ' or 'არ'.")
#        response = input(kitxva + " (დიახ/არა): ").strip().lower()
#    return response
#
#print("გამარჯობა! მოდი ვიპოვოთ თქვენთვის შესაფერისი პროფესია.")
#
#k1_pasuxi = kitxva("ხელსაყრელია ხალხთან მუშაობა?")
#k2_pasuxi = kitxva("კარგი ხართ პრობლემების გადაჭრაში?")
#k3_pasuxi = kitxva("დამოუკიდებლად მუშაობა გირჩევნიათ?")
#k4_pasuxi = kitxva("გაინტერესებთ ტექნოლოგიები და კომპიუტერები?")
#k5_pasuxi = kitxva("მოგწონთ ფიზიკური აქტივობა და პრაქტიკული მუშაობა?")
#k6_pasuxi = kitxva("ხართ შემოქმედებითი და გსიამოვნებთ მხატვრული საქმიანობა?")
#k7_pasuxi = kitxva("კარგი ხართ კომუნიკაციასა და მოლაპარაკებაში?")
#
#
#if k1_pasuxi == "დიახ":
#    if k2_pasuxi == "დიახ":
#        profesia = "გამყიდველი"
#    else:
#        profesia = "მასწავლებელი"
#else:
#    if k3_pasuxi == "დიახ":
#        if k5_pasuxi == "დიახ":
#            profesia = "მექანიდი"
#        else:
#            profesia = "ბუღალტერი"
#    else:
#        if k4_pasuxi == "დიახ":
#            profesia = "პროგრამერი"
#        elif k6_pasuxi == "დიახ":
#            profesia = "არტისტი"
#        else:
#            profesia = "დატა ანალისტი"
#
#print(f"თქვენი პასუხებიდან გამომდინარე, შესაძლოა თქვენთვის შესაფერისი პროფესია იყოს: {profesia}")



