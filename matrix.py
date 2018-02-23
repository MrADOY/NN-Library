class Matrix(object):
    """Represent a matrix , mainly to perform matrix operations"""

    def __init__(self, rows, cols):
        """Initialize the matrix (rows x cols) with 0 """
        self.rows = rows
        self.cols = cols
        self.values = [[0 for _ in range(cols)] for _ in range(rows)]

    def scalar_multiply(self, n):
        """Mutiply all the values by n"""
        for i in range(self.rows):
            for j in range(self.cols):
                self.values[i][j] *= n

    def scalar_addition(self, n):
        """Addition all the values by n"""
        for i in range(self.rows):
            for j in range(self.cols):
                self.values[i][j] *= n
