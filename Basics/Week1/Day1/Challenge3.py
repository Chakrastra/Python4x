#Write a Pbthon function that acts as a simple calculator, performing addition, subtraction, multiplication, and division based on user input. 

a = float(input("Enter num1="))
b = float(input("Enter num2="))

Opr=(input("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n Enter the number acc to operation: "))
match Opr :
    case '1':
        print(a+b)

    case '2':
        print(a-b)

    case '3':
        print(a*b)

    case '4':
        print(a/b)

    case _:
        print("Enter a valid opration.")