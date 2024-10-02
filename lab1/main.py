print('''Лабораторна робота №1
  Тема: Програмування лінійних алгоритмів та розгалуджених процесів
  Мета роботи:  Придбання навичок по роботі з інтегрованим середовищем Python  IDLE. Вивчення  принципів  розробки  програм  лінійної  структури. Отримання навичок роботи з функціями уведення / виведення, різними типами даних,  прийнятих  в  цій  мові.  Вивчення  керуючих  структур  мови  Python  і отримання навичок складання програм з розгалуженнями.
Виконав студент Латко Артем, група КМ-32, варіант 11
Умови завдань:
1. Вивести на екран букву "W" з символів "*" (зірочка).
2. Послуги телефонної мережі оплачуються за таким правилом: за розмови до А хвилин в місяць - В грн., а розмови понад встановлену норму оплачуються з розрахунку З грн за хвилину. Написати програму, яка обчислює плату за користування телефоном для уведеного часу розмов за місяць. Дані вводити з клавіатури.
3. F(x) = { 4x^2 + 2x - 19, якщо x >= -3.5;
          { -2x/(-4x + 1)  , якщо x < 3.5; 
           ''')




while True:
    try:
        choice = int(input('''
Enter the number of task(1, 2 or 3) or enter 0 to exit: '''))
        #TASK 2
        if choice == 2:
            print('''
Task 2''')
            while True:
                try:
                    minutes_per_month = int(input("Enter the total number of talk minutes per month: "))
                    if minutes_per_month >= 0:
                        break
                        print(choice)
                    else:
                        print("Please enter a valid positive integer for the number of minutes")
                except ValueError:
                    print("Please enter a valid positive integer for the number of minutes")

            while True:
                try:
                    norm_of_minutes = int(input("Enter the norm of minutes per month: "))
                    if norm_of_minutes >= 0:
                        break
                    else:
                        print("Please enter a valid positive integer for the number of minutes")
                except ValueError:
                    print("Please enter a valid positive integer for the norm of minutes")
      
            while True:
                try:
                    not_exceeding_the_norm = float(input("Enter the cost(for one minute) of a call, which does not exceed the norm of minutes per month in the range (0; 3): "))
                    if not_exceeding_the_norm < 3.0 and not_exceeding_the_norm > 0.0:
                        break
                    else:
                        print("Does not match the gap")
                except ValueError:
                    print("Does not match the gap")
#As a condition, we indicate that for exceeding the price per minute is 3 grn.
            exceeding_the_norm = 3 
#Using the if operator, we will calculate the cost of calls per month
            if minutes_per_month > norm_of_minutes:
                price_per_month = round(norm_of_minutes * not_exceeding_the_norm + (minutes_per_month - norm_of_minutes) * exceeding_the_norm, 3)
                print("Price per month: %s" % price_per_month)
            elif minutes_per_month <= norm_of_minutes:
                price_per_month = round(norm_of_minutes * not_exceeding_the_norm, 3)
                print("Price per month: %s" % price_per_month)
        #TASK 1
        if choice == 1:
            print('''
TASK 1''')
            print('''
                 *             *
                  *           *
                   *    *    *
                    *  * *  *
                     **   **     
                         
                         ''')
        if choice == 3:
            print('''
TASK 3''')
#We set an arbitrary value of x
            while True:
                try:
                    x = float(input("Enter the value of x: "))
                    if x >= -3.5:
                        result_1 = round(4*x**2 + 2*x - 19, 3)
                        print("4x^2 + 2x - 19 = %s" % result_1)
                    if x < 3.5:
                        result_2 = round(-2*x/(-4*x + 1), 3)
                        print("-2x/(-4x + 1) = %s" % result_2)
                        break
                except ValueError:
                    print("Specify the value of x that belongs to real numbers")
        if choice == 0:
            import os
            import time
            os.system("clear")
            print('EXIT')
            time.sleep(3)
            os.system("clear")
            break
    except ValueError:
        print("It's not 1, 2, 3 or 0")


'''
                Latko Artem. KM-32
'''