    #davaleba1
#a = input("input: ")
#b = a * 3
#print("output:", b)



    #davaleba2
#weight = int(input("Enter your weight in killograms: "))
#
#moon_weight = weight / 6
#
#print( "Your weight on the Moon would be", moon_weight, "kg")



    #davaleba3
def calculator(user_input):
    try:
        components = user_input.split()
        if len(components) != 3:
            return "Invalid input. Please provide input in the format 'number1 operation number2'."

        number1 = float(components[0])
        operation = components[1]
        number2 = float(components[2])

        if operation == '+':
            result = number1 + number2
        elif operation == '-':
            result = number1 - number2
        elif operation == '*':
            result = number1 * number2
        elif operation == '/':
            if number2 == 0:
                return "Division by zero is not allowed."
            result = number1 / number2
        elif operation == '^':
            result = number1 ** number2
        else:
            return "Invalid operation. Valid operations are +, -, *, /, and ^."

        return result

    except ValueError:
        return "Invalid input. Please enter valid numbers."
    except Exception as a:
        return input("An error occurred:", {str(a)})

user_input = input("Enter an equation: ")

calculation_result = calculator(user_input)
print(calculation_result)
