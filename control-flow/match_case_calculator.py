num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operator = input("Choose the operation (+, -, *, /):")

# performing calculations using match case
match operator:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            exit()                                                                          ;
    case _:
        print("Invalid operator")
        exit()
        
print(f"The result is {result}")