
#Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

result = {}
with open('test_5.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        hours = 0
        for elem in data[1:]:
            if elem != '-':
                num = '0'
                for i in elem:
                    if i.isdigit():
                        num += i
                    else:
                        break
                hours += int(num)
        result.update({data[0].strip(':'): hours})
print(result)


