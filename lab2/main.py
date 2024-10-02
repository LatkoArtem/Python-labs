print('''Лабораторна робота №2
Тема: ПРОГРАМУВАННЯ ЦИКЛІЧНИХ АЛГОРИТМІВ
Мета роботи: Вивчення засобів реалізації циклічних конструкцій мови Python і отримання навичок складання програм з використанням операторів циклу.
Виконав студент Латко Артем, група КМ-32, варіант 11
Умови завдань:
              n
1. Обчислити  ∑(x-і)^2
             i=1
2. Дано додатні числа A і B (A>B). На відрізку довжиною A розміщено максимально можлива кількість відрізків довжиною B (без накладання). Не використовуючи операції множення і ділення, знайти кількість відрізків B, розміщених на відрізку A.'''
      )

while True:
  try:
    choice = int(
        input('''
Enter the number of task(1 or 2) or enter 0 to exit: '''))
    #TASK 1
    if choice == 1:
      print('''
Task 1''')
      #set the value for 'x' and 'n'
      while True:
        try:
          n = int(input("Enter the value of 'n': "))
          if n >= 1:
            break
          else:
            print("Please enter a natural number")
        except ValueError:
          print("Please enter a natural number")

      while True:
        try:
          x = float(input("Enter the value of 'x': "))
          break
        except ValueError:
          print("Specify the value of x that belongs to real numbers")
      #calculate the formula using the "for cycle"
      sum = 0
      for i in range(1, n + 1):
        sum += (x - i)**2
        round(sum, 4)
      print('Answer: %s' % sum)

    if choice == 2:
      print('''
Task 2''')
      while True:
        try:
          A = float(input("Enter the positive value of A: "))
          if A > 0:
            break
          else:
            print("The number must be positive")
        except ValueError:
          print("Is not a positive value of A")

      while True:
        try:
          B = float(input("Enter the positive value of B(B<A): "))
          if B < A:
            break
          else:
            print("The number must be positive and less then A")
        except ValueError:
          print("Is not a positive value of B")

      answer = 0
      while A >= B:
        A -= B
        answer += 1
      print("Answer: %s" % answer)

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
  except ValueError:
    print("It's not 1, 2 or 0")
'''
                Latko Artem. KM-32
'''
