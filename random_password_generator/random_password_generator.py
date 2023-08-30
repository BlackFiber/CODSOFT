import random

num_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

letter_tup=('A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N'
                  'n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z')

special_tup=('!','@','#','$','%','^','&','*','(',')','{','}','[',']'
                 ,',','.','/','-','+','_','=')


#random number generator
num_list=[]
def inclu_num():
    for i in range(pass_len):
         num_list.append(random.choice(num_tup))
    for i in range(len(num_list)):
        print(num_list[i],end='')

#random letter generator
letter_list=[]
def inclu_letter():
    for i in range(pass_len):
         letter_list.append(random.choice(letter_tup))
    for i in range(len(letter_list)):
        print(letter_list[i],end='')

#random special character generator
special_list=[]
def inclu_special():
    for i in range(pass_len):
         special_list.append(random.choice(special_tup))
    for i in range(len(special_list)):
        print(special_list[i],end='')

print("\t\t---***\\\\\\\\\\ RANDOM PASSWORD GENERATOR /////***---")

pass_len=int(input("\nEnter the length of the password you want : "))

print("\nAnswer all the question using y(y for yes) or n(n for no)!!!!\n")

dis_num=input("Do you want to include number :  ")
dis_letter=input("Do you want to include letter : ")
dis_special_char=input("Do you want to include special characters : ")

if dis_num=="y"  and dis_letter=="n"  and dis_special_char=="n" :
    inclu_num()

elif dis_num=="n"  and dis_letter=="y"  and dis_special_char=="n" :
    inclu_letter()

elif dis_num=="n"  and dis_letter=="n"  and dis_special_char=="y" :
    inclu_special()

elif dis_num=="y"  and dis_letter=="y"  and dis_special_char=="n" :
    num_letter_list=[]
    num_letter_list=num_tup+letter_tup
    pass_num_letter=[]

    for i in range(pass_len):
       pass_num_letter.append(random.choice(num_letter_list))
    for i in range(len(pass_num_letter)):
       print(pass_num_letter[i],end='')

elif dis_num=="y" and dis_letter=="n"  and dis_special_char=="y" :
    num_special_list=[]
    num_special_list=num_tup+special_tup
    pass_num_special=[]

    for i in range(pass_len):
       pass_num_special.append(random.choice(num_special_list))
    for i in range(len(pass_num_special)):
       print(pass_num_special[i],end='')

# password made with letter and special
elif dis_num=="n" and dis_letter=="y"  and dis_special_char=="y" :
    letter_special_list=[]
    letter_special_list=letter_tup+special_tup
    pass_letter_special=[]

    for i in range(pass_len):
       pass_letter_special.append(random.choice(letter_special_list))
    for i in range(len(pass_letter_special)):
       print(pass_letter_special[i],end='')


# password made with number,letter and special characters
elif dis_num=="y" and dis_letter=="y"  and dis_special_char=="y" :
    num_letter_special_list=[]
    num_letter_special_list=letter_tup+special_tup+num_tup
    pass_num_letter_special=[]

    for i in range(pass_len):
       pass_num_letter_special.append(random.choice(num_letter_special_list))
    for i in range(len(pass_num_letter_special)):
       print(pass_num_letter_special[i],end='')





