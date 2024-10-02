import numpy as np
import os
import time
print('''Лабораторна робота №6
Тема: РЕКУРСІЯ ТА ОБРОБКА МАТРИЦЬ
Мета роботи: Вивчення роботи з одновимірними і двовимірними масивами із застосуванням рекурсивних функцій. 
Виконав студент Латко Артем, група КМ-32, варіант 11

Умова завдання:        	     
1. Дан одновимірний масив числових значень, що нараховує n елементів. Визначити, чи утворюють елементи масиву, розташовані перед першим від'ємним елементом, спадаючу послідовність.
2. Виконати обробку елементів прямокутної матриці A, що має n рядків і m стовпців. Підсумувати елементи кожного рядка матриці з відповідними 
елементами k-го рядка.''')
while True:
    try:
        choice = int(input('''
Enter the number of task 1, 2 or enter 0 to exit: '''))
        #TASK 1
        if choice == 1:
            while True:
                try:
                    n = int(input('Enter the number of elements: '))
                    if n >= 1:
                        break
                    else:
                        print("The number of numbers can only be specified using natural numbers")
                except ValueError:
                    print("The number of numbers can only be specified using natural numbers")
                  
            print('''
Specify the lower and high limits so that it then generates a random numbers no lower and no high than you specified.
''')
            
            while True:
                try:
                    low = int(input("Specify the lower limit: "))
                    break
                except ValueError:
                    print("Enter the integer")

            while True:
                try:
                    high = int(input("Specify the high limit: "))
                    if high > low:
                        break
                    else:
                        print("The high limit must be greater than the lower limit")
                except ValueError:
                    print("Enter the integer")
                  
            array = np.random.randint(low, high, n)
            print(f"The array is: {array}")

            def decreasing_before_neg_num(array, i=0):
                if array[i] < 0:
                    return True
                  
                if i > 0 and array[i] >= array[i - 1]:
                    return False
                  
                return decreasing_before_neg_num(array, i + 1)

            if all(el >= 0 for el in array):
                print("The array does not contain negative numbers at all")
            elif array[0] < 0 or array[1] < 0:
                print("It is not possible to check")
            else:
                if decreasing_before_neg_num(array):
                    print("The array has a decreasing sequence before the first negative number")
                else:
                    print("The array does not have a decreasing sequence before the first negative number")

        #TASK 2
        elif choice == 2:
            while True:
                try:
                    n = int(input("Enter the number of rows: "))
                    if n >= 1:
                        break
                    else:
                        print("The number of rows can only be specified using natural numbers")
                except ValueError:
                    print("The number of rows can only be specified using natural numbers")

            while True:
                try:
                    m = int(input("Enter the number of columns: "))
                    if m >= 1:
                        break
                    else:
                        print("The number of columns can only be specified using natural numbers")
                except ValueError:
                    print("The number of columns can only be specified using natural numbers")

            print('''
Specify the lower and high limits so that it then generates a random numbers no lower and no high than you specified.
            ''')
            
            while True:
              try:
                  low = int(input("Specify the lower limit: "))
                  break
              except ValueError:
                  print("Enter the integer")

            while True:
              try:
                  high = int(input("Specify the high limit: "))
                  if high > low:
                      break
                  else:
                      print("The high limit must be greater than the lower limit")
              except ValueError:
                  print("Enter the integer")

            array = np.random.randint(low, high, (n, m))
            print(f'''Matrix:
{array}''')

            while True:
                try:
                    k = int(input("Enter the row you want to add: "))
                    if k >= 1 and k <= n:
                        break
                    else:
                        print("The 'k' number can only be specified using natural numbers and be less than the number of rows")
                except ValueError:
                    print("Enter the integer")
                  
            def sum_rows(array, k, i=0):
                for i in range(len(array)):
                    if i != k - 1:
                        for j in range(len(array[i])):
                            array[i][j] += array[k-1][j]

            sum_rows(array, k)

            print(f"Matrix after adding {k} row:")
            print(f"{array}")
        #EXIT
        #EXIT   
        elif choice == 0:
            os.system("clear")
            print('EXIT')
            time.sleep(3)
            os.system("clear")
            break

        else:
            print("It's not 1, 2 or 0")
    except ValueError:
        print("It's not 1, 2 or 0")
'''
                Latko Artem. KM-32
'''