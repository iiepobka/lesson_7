# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__() ), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        line = ''
        count = 0
        for i in range(len(self.matrix)):
            for item in range(len(self.matrix[i])):
                count += 1
                if count % len(self.matrix) == 0:
                    line += str(self.matrix[i][item]) + '\n'
                else:
                    line += str(self.matrix[i][item]) + ' '
        return f'{line}'

    def __add__(self, other):
        line = ''
        count = 0
        for i in range(len(self.matrix)):
            for item in range(len(self.matrix[i])):
                count += 1
                if count % len(self.matrix) == 0:
                    line += str(self.matrix[i][item] + other.matrix[i][item]) + '\n'
                else:
                    line += str(self.matrix[i][item] + other.matrix[i][item]) + ' '
        return f'{line}'


m_1 = Matrix([[1, 2, 3, 4], [4, 5, 6, 5], [7, 8, 9, 6], [4, 5, 6, 9]])
m_2 = Matrix([[2, 5, 7, 1], [0, 1, 0, 1], [2, 6, 5, 10], [12, 7, 6, 1]])
print(f'Первая матрица:\n{m_1}')
print(f'Вторая матрица:\n{m_2}')
print(f'Сумма двух матриц:\n{m_2 + m_1}')
