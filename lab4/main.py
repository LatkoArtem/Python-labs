print('''Лабораторна робота №4
Тема: РЯДКИ
Мета роботи: Вивчення типу даних String, функцій і модулів, які використовуються для обробки даних цього типу.
Виконав студент Латко Артем, група КМ-32, варіант 11

Умова завдання:        	     
1. Вставити пробіл після перших 2-х символів в слова, що мають довжину, на 1 менше заданої.''')
import re
while True:
    try:
        choice = int(input('''
Enter the number of task 1 or enter 0 to exit: '''))
        #TASK 1
        if choice == 1:
            print('''
Task 1
''')
            while True:
                try:
                    number_of_words = int(input("Enter the number of words: "))
                    if number_of_words > 0:
                        break
                    else:
                        print("Enter a natural number to specify the number of words")
                except:
                    print("Enter a natural number to specify the number of words")

            while True:
                try:
                    length_of_words = int(input("Enter the max length of the words: "))
                    if length_of_words > 0:
                        break
                    else:
                        print("Enter a natural number for the word length")
                except ValueError:
                    print("Enter a natural number for the word length")
                  
            while True:
                text = input("Enter a text: ")
                words = re.findall(r'\w+|\W+', text)
                alpha_elements = 0
                for word in words:
                    if isinstance(word, str) and word.isalpha():
                        alpha_elements += 1
                if alpha_elements == number_of_words:
                    if all(len(word) <= length_of_words for word in words):
                        break
                    else:
                        print("The word length is more than the specified length")
                else:
                    print("Enter the number of words in the text as much as indicated earlier")

            text_list = []
            for word in words:
                if len(word) < length_of_words and word.isalpha():
                    word = word[:2] + ' ' + word[2:]
                text_list.append(word)   
            print(text_list)
            new_text = ''.join(text_list)
            print(f"Result: {new_text}")


        if choice == 0:
            import os
            import time
            os.system("clear")
            print('EXIT')
            time.sleep(3)
            os.system("clear")
            break


        if choice < 0:
            print("It's not 1 or 0")
        if choice > 1:
            print("It's not 1 or 0")

    except ValueError:
        print("It's not 1 or 0")
'''
                Latko Artem. KM-32
'''