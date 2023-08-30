def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

prev_result=[]
def calculation():
    n1=int(input("Enter the 1st number : "))
    opt=input("Choose any one operation between +,-,* & / : ")
    n2=int(input("Enter the 2nd number : "))
    match opt:
        case '+':
            print("Sum of ", n1, " and ", n2, " = ", addition(n1,n2))
            prev_result.append(addition(n1,n2))


        case '-':
            print("Difference between ", n1, " and ", n2, " = ", subtraction(n1,n2))
            prev_result.append(subtraction(n1,n2))

        case '*':
            print("Result, after performing mulplication between ",n1," and ",n2," = ",multiplication(n1,n2))
            prev_result.append(multiplication(n1, n2))

        case '/':
            print("Result, after performing devision operatoin between ", n1, " and ", n2, " = ", division(n1,n2))
            prev_result.append(division(n1, n2))



        case default:
            print("Sorry!!!, i am unable to understand your command. \nPlease try again with proper input.")

print("\t\t\t--**\\\\\\\\\\ SIMPLE - CALCULATOR /////**--")
opr=int(input("How many operation you want to perform : "))


for i in range(opr):
    print("\n\t\t--*** ------------------------------ ***--\n")
    calculation()
    print("\n")
    for j in range(len(prev_result)):
        print(j+1, " no. calculation result = ",prev_result[j])
    print("\n\t\t--*** ------------------------------ ***--\n")

prev_result.clear()


