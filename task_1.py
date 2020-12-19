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
        if not isinstance(other, Matrix):
            raise ValueError('Правый операнд не класса Matrix')

        sum_matrix = []
        for m in range(len(self.value)):
            row = list(map(lambda x, y: x + y, self.value[m], other.value[m]))
            sum_matrix.append(row)

        return Matrix(sum_matrix)

matrix_one = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix_two = [
    [8, 5, 4],
    [3, 2, 3]
]

m = Matrix(matrix_one)
n = Matrix(matrix_two)
print(m + n)
