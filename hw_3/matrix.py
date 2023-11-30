import hashlib


class HashableMixin:
    def __hash__(self):
        # преобразовываем данные в одну большую строчку
        flattened_data = [str(item) for row in self.data for item in row]
        concatenated_data = ''.join(flattened_data)
        # возвращаем кэш полученной строки
        return concatenated_data.__hash__()


class Matrix(HashableMixin):
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")

        result_data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result_data)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError(
                    "Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

            result_data = [
                [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)]
                for i in range(self.rows)
            ]
            return Matrix(result_data)
        else:
            result_data = [[self.data[i][j] * other for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(result_data)

    def __matmul__(self, other):
        return self.__mul__(other)
