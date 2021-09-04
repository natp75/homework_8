
#Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.



with open('test.txt', 'w') as file:
    input_line = input('Text: \n')
    while input_line:
        file.write(f'{input_line}\n')
        input_line = input('Text: \n')