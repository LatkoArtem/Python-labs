import os
import time
print('''Лабораторна робота №7
Тема: РОБОТА З ФАЙЛАМИ
Мета роботи: Вивчення методів роботи з файлами та придбання практичних навичок створення і обробки текстових файлів. 
Виконав студент Латко Артем, група КМ-32, варіант 11

Умова завдання:        	     
1. Вивести на екран построково текстовий файл, вставляючи в початок 
кожного рядка його порядковий номер (він повинен займати 4 позиції) і 
пробіл.''')
while True:
    try:
        choice = int(input('''
Enter the number of task 1 or enter 0 to exit: '''))
        #TASK 1
        if choice == 1:
            text = 'Text.txt'
            with open(text, 'r') as file:
                lines = file.readlines()
                #according to the condition before the task
                len_of_line = 80
                i = 1
                for line in lines:
                    for letter in range(0, len(line), len_of_line):
                        print(f'{i:4d} {line[letter:letter+len_of_line]}', end='\n')
                        i += 1

        #EXIT   
        elif choice == 0:
            os.system("clear")
            print('EXIT')
            time.sleep(3)
            os.system("clear")
            break

        else:
            print("It's not 1 or 0")
    except ValueError:
        print("It's not 1 or 0")
'''
                Latko Artem. KM-32
'''