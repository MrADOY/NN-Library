import random as rd


class Matrix(object):
    """Represent a matrix , mainly to perform matrix operations"""

    def __init__(self, rows, cols):
        """Initialize the matrix (rows x cols) with 0 """
        self.rows = rows
        self.cols = cols
        self.values = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return "{}".format(self.values)

    def randomize(self):
        """Initialize matriw with random values"""
        for i in range(self.rows):
            for j in range(self.cols):
                self.values[i][j] = rd.uniform(-1, 1)

    @staticmethod
    def multiply(m1, m2):
        """return new matrix with dot product of m1 & m2"""
        if m1.cols != m2.rows:
            print('Columns of A must match rows of B')
            return
        else:
            result = Matrix(m1.rows, m2.cols)
            for i in range(result.rows):
                for j in range(result.cols):
                    s = 0
                    for k in range(m1.cols):
                        s += m1.values[i][k] * m2.values[k][j]
                    result.values[i][j] = s
            return result

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

    def map(self, f):
        """Apply function to each element of m"""
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.values[i][j]
                self.values[i][j] = f(val)

    @staticmethod
    def fromArray(arr):
        """Convert a array to a matrix object"""
        m = Matrix(len(arr), 1)
        for i in range(len(arr)):
            m.values[i][0] = arr[i]
        return m

    def toArray(self):
        """Convert a matrix object to a array"""
        arr = []
        for i in range(self.rows):
            for j in range(self.cols):
                arr.append(self.values[i][j])
        return arr
