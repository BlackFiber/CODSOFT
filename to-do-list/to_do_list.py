def show_tasks():
    with open('to_do_list.txt') as tasks :
        list=tasks.read()
        print(list)


def add_tasks():
    with open("to_do_list.txt") as list:
        lines = list.readlines()

    sl_no = len(lines)
    task=input("Enter new task : ")
    f_task=str(sl_no+1)+". "+task+'.\n'


    with open('to_do_list.txt','a') as tasks :
        tasks.write(f_task)



def delete_tasks():
    print('\n\n')
    show_tasks()
    print('\n')
    new_lines = []
    task_number=int(input("Enter the sl no. of the task you want to delete : "))
    with open("to_do_list.txt") as list:
        lines = list.readlines()

    for line in lines:
        if line[0]==(str(task_number)):
            continue
        else:
            new_lines.append(line)

    with open("to_do_list.txt", 'w') as list:
        list.write('')
    for ele in new_lines:
        with open("to_do_list.txt", 'a') as list:
            list.write(ele)
        print(ele,end="")
    print('--***---------  After Deletion  ---------***--')
    show_tasks()
    print('\n\n')


def del_entire_list():
    with open("to_do_list.txt", 'w') as list:
        list.write('')
    with open("complete_task.txt", 'w') as list:
        list.write('')

def replace_task():
    print('\n\n')
    show_tasks()
    print('\n')
    replace_lines = []
    with open('to_do_list.txt') as f:
         lines=f.readlines()
    for line in lines:
        replace_lines.append(line)

    r_t_sl=int(input('Enter the sl no. of the task, which you want to replace : '))
    r_task=input('Enter the new task : ')
    replace_lines[r_t_sl-1]= str(r_t_sl)+". "+r_task+".\n"

    with open('to_do_list.txt','w') as f:
        f.write("")
    for ele in replace_lines:
        with open("to_do_list.txt", 'a') as list:
            list.write(ele)
        print(ele,end="")
    print('--***---------  After Replacement  ---------***--')
    show_tasks()
    print('\n\n')


def com_task():
    print('\n\n')
    show_tasks()
    print('\n')
    task_number = int(input("Enter the sl no. of the task you want to mark as complete : "))
    with open("to_do_list.txt") as list:
        lines = list.readlines()

    for line in lines:
        if line[0] == (str(task_number)):
            with open("complete_task.txt",'a') as list:
                lines = list.write(line)
        else:
            continue


    new_lines = []
    with open("to_do_list.txt") as list:
        lines = list.readlines()

    for line in lines:
        if line[0] == (str(task_number)):
            continue
        else:
            new_lines.append(line)

    with open("to_do_list.txt", 'w') as list:
        list.write('')
    for ele in new_lines:
        with open("to_do_list.txt", 'a') as list:
            list.write(ele)
        print(ele, end="")

    print('--***---------  After Mark Completed Task  ---------***--')
    show_tasks()
    print('\n\n')


print('\t\t\t--**\\\\\\\\\\ TO - DO - LIST /////**--\nOPTIONS : ')
print('1. ADD TASK \n2. DELETE TASK \n3. DELETE ENTIRE LIST \n4. SHOW TASK LIST\n5. REPLACE TASK'
      '\n6. MARK AS COMPLETE TASK \n7. SHOW COMPLETED TASK LIST')
job=int(input('Choose any one option by the entering it\'s sl no : '))

if job==1:
    q_task=int(input('How much task you want to enter in the list : '))
    for t in range(q_task):
        add_tasks()

elif job==2:
    q_task=int(input('How much task you want to delete : '))
    for t in range(q_task):
        delete_tasks()

elif job==3:
    del_entire_list()
    print('The entire To-Do-List is empty now. ')

elif job==4:
    show_tasks()

elif job==5:
    q_task = int(input('How much task you want to replace : '))
    for t in range(q_task):
        replace_task()


elif job==6:
    q_task = int(input('How much task you want to mark as complete : '))
    for t in range(q_task):
        com_task()

elif job==7:
    with open('complete_task.txt')as f:
        txt=f.read()
    print('\n',txt,'\n')
else:
    print('Sorry!!!. I am unable to understand your command. \nPlease try with proper input.')


