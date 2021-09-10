
#Реализовать класс ​Matrix (​матрица). Обеспечить перегрузку конструктора класса (метод __init__())​,
#который должен принимать данные (список списков) для формирования матрицы.
#Подсказка: матрица — ​система некоторых математических величин, расположенных в виде прямоугольной схемы.
#Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#31  22          3    5    32        3   5   8   3
#37  43          2    4    6         8   3   7   1
#51  86         -1   64   -8
#Следующий шаг — реализовать перегрузку метода ​__str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода ​__add__() для реализации операции сложения двух объектов класса ​Matrix (​двух матриц).
#Результатом сложения должна быть новая матрица.
#Подсказка: сложение элементов матриц выполнять поэлементно —
#первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    value: list

    def __init__(self, value: list):
        self.value = value

    def __add__(self, other: 'Matrix'):
        try:
            rows_count = len(self.value)
            items_count = len(self.value[0])

            new_value = [
                [
                    self.value[row][idx] + other.value[row][idx]
                    for idx in range(items_count)
                ]
                for row in range(rows_count)
            ]

            return Matrix(new_value)
        except IndexError:
            print("Ошибка - Матрицы разного размера")
            exit(1)

    def __str__(self):
        return "\n".join(
            str(row).strip('[]').replace(',', '')
            for row in self.value
        )


a = Matrix([
    [11, 12, 13],
    [14, 15, 16],
])

b = Matrix([
    [21, 22, 23],
    [24, 25, 26],
])

c = a + b

print(c)