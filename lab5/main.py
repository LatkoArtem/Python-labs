print('''Лабораторна робота №4
Тема: ВИКОРИСТАННЯ ФУНКЦІЙ
Мета роботи: Вивчення написання і застосування функцій на мові Python 
Виконав студент Латко Артем, група КМ-32, варіант 11

Умова завдання:        	     
1. На площині задано кільце з центром в точці (х0, у0), внутрішнім радіусом r1 і зовнішнім r2. Скласти функцію, яка для заданого масиву точок ХY обчислює кількість  точок,  що  належать  кільцю.  Точки,  розташовані  на  межі кільця, вважати належним кільцю.
2. Функція - Pos(s,s1). Призначення - пошук першого входження підрядка s1 у рядок s.''')
while True:
    try:
        choice = int(input('''
Enter the number of task 1, 2 or enter 0 to exit: '''))
        #TASK 1
        if choice == 1:
            import math
            def points_in_ring(xy_array, x0, y0, r1, r2):
                def point_in_ring(x, y):
                    #Використовую math.sqrt лише для того щоб порахувати двадратний корінь
                    distance = math.sqrt((x - x0)**2 + (y - y0)**2)
                    return r1 <= distance <= r2

                # Обчислення кількості точок, що належать кільцю
                count = 0
                for point in xy_array:
                    x, y = point
                    if point_in_ring(x, y):
                        count += 1

                return count

            while True:
                try:
                    x0 = float(input("Enter the x0 coordinate of the center of the ring: "))
                    if x0.is_integer:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")
                  
            while True:
                try:
                    y0 = float(input("Enter the y0 coordinate of the center of the ring: "))
                    if y0.is_integer:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")
                  
            while True:
                try:
                    r1 = float(input("Enter the inner radius of the ring: "))
                    if r1 <= 0:
                        print("The inner radius must be greater than 0")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number")
                  
            while True:
                try:
                    r2 = float(input("Enter the outer radius of the ring: "))
                    if r2 <= 0:
                        print("The outer radius must be greater than 0")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number")
                  
            xy_array = []
            while True:
                try:    
                    number_of_points = int(input("Enter the number of points for XY array: "))
                    if number_of_points <= 0:
                        print("The number of points must be greater than 0")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number")
            for i in range(number_of_points):
                while True:
                    try:  
                        x = float(input(f"Enter the x coordinate of point {i+1}: "))
                        if x % 1 == 0:
                            x = int(x)
                            break
                        else:
                            break
                    except ValueError:
                        print("Invalid input. Please enter a number")
                while True:
                    try: 
                        y = float(input(f"Enter the y coordinate of point {i+1}: "))
                        if y % 1 == 0:
                            y = int(y)
                            break
                        else:
                            break
                    except ValueError:
                        print("Invalid input. Please enter a number")
                xy_array.append((x, y))
                      
            print(f"XY array: {xy_array}")
            result = points_in_ring(xy_array, x0, y0, r1, r2)
            print(f"The number of points belonging to the ring: {result}")

        #TASK 2
        if choice == 2:
            def pos(s, s1):
              if s.find(s1) != -1:
                  print(f"The first occurrence of the substring '{s1}' in string '{s}' is at position {s.find(s1) + 1}")
              else:
                  print(f"The substring '{s1}' is not found in string '{s}'.")
            s = input("Enter the string: ")
            s1 = input("Enter the substring: ")
            pos(s, s1)       
            
        #EXIT   
        if choice == 0:
            import os
            import time
            os.system("clear")
            print('EXIT')
            time.sleep(3)
            os.system("clear")
            break


        if choice < 0:
            print("It's not 1, 2 or 0")
        if choice > 2:
            print("It's not 1, 2 or 0")

    except ValueError:
        print("It's not 1, 2 or 0")
'''
                Latko Artem. KM-32
'''