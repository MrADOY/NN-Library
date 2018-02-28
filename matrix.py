import random as rd


class Matrix(object):
    """Represent a matrix , mainly to perform matrix operations"""

    def __init__(self, rows, cols):
        """Initialize the matrix (rows x cols) with 0 """
        self.rows = rows
        self.cols = cols
        self.values = [[0 for _ in range(cols)] for _ in range(rows)]

    def randomize(self):
        """Initialize matriw with random values"""
        for i in range(self.rows):
            for j in range(self.cols):
                self.values[i][j] = int(rd.uniform(0, 10))

    def multiply(self, n):
        """Mutiply all the values by n if n is a value
        or do the dot product if n if a matrix"""

        if isinstance(n, Matrix):
            if self.cols != n.rows:
                print('Columns of A must match rows of B')
                return
            else:
                result = Matrix(n.rows, self.cols)
                for i in range(self.rows):
                    for j in range(self.cols):
                        s = 0
                        for k in range(self.cols):
                            s += self.values[i][k] * n.values[k][j]
                        result.values[i][j] = s
                return result
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.values[i][j] *= n

    def addition(self, n):
        """Add to all the values n if n is a value
        or addition between m and n if n is a matrix"""

        if isinstance(n, Matrix):
            for i in range(self.rows):
                for j in range(self.cols):
                    self.values[i][j] += n.values[i][j]

        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.values[i][j] += n

    def transpose(self):
        """ Return the transpose of self """
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.values[i][j] = self.values[j][i]
        return result
