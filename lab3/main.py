print('''Лабораторна робота №3
Тема: СТРУКТУРИ ДАНИХ: СПИСКИ, КОРТЕЖИ, МНОЖИНИ
Мета роботи:Вивчення структур даних (list, tuple, set), створюваних користувачем.
Виконав студент Латко Артем, група КМ-32, варіант 11
Умови завдань:
              	     
1. Створити список, елементами якого будуть слова. Необхідно: 
- підрахувати, скільки разів кожен символ зустрічається у списку; 
- створити новий список, елементами якого будуть вкладені списки, що складаються з двох елементів: символ і кількість його повторень  у вихідному списку. Наприклад, ['s', 10]; 
- упорядкувати новий список або по символу або по числу; 
- типом даних dict у цьому завданні не користуватися.
2. A = {1, 2, ee, ww, a, d}, B = {2, a, b, tt, 4, 3}, F = ((A + B) ∪ (A \ B))''')


while True:
    try:
        choice = int(input('''
Enter the number of task(1 or 2) or enter 0 to exit: '''))
        #TASK 1
        if choice == 1:
            print('''
Task 1
''')
            while True:
                words = input("Enter the elements, separating them with commas (', '), and ensure that each element contains only letters: ")
                inp = words.rstrip(', ').split(', ')
                all_alpha = all(word.isalpha() for word in words.split(', '))
                if not all_alpha:
                    print("One or more elements do not contain only letters. Please try again.")
                else:
                    break
            word_list = [w for w in words.split(', ')]
            list_of_simbols = []
            for word in word_list:
                for simbol in word:
                    simbol_exists = False
                    for item in list_of_simbols:
                        if item[0] == simbol:
                            item[1] += 1
                            simbol_exists = True
                            break
                    if not simbol_exists:
                        list_of_simbols.append([simbol, 1])
                
            print("List of symbols and their quantities:", list_of_simbols)
  
            list_of_simbols.sort()
            print('''
Sorted list by symbol:''', list_of_simbols)
        #TASK 2
        if choice == 2:
            print('''
Task 2
''')
            A = {1, 2, 'ee', 'ww', 'a', 'd'}
            B = {2, 'a', 'b', 'tt', 4, 3}
            F = ((A ^ B) | (A - B))
            print("F = ((A + B) ∪ (A \ B)) =", F)


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