"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__() ), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Пример матрицы: 2 на 3
1 0 1
1 1 0
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str('\n'.join([' '.join([str(i) for i in j]) for j in self.value]))

    def __add__(self, other):
        rows = len(self.value)
        cols = len(self.value[0])
        print(rows, cols)
        res = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(self.value[i][j] + other[i][j])
            res.append(row)
        return res


matrix_one = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix_two = [
    [6, 5, 4],
    [3, 2, 1]
]

m = Matrix(matrix_one)
n = Matrix(matrix_two)
print(m)

# print(m + n)
