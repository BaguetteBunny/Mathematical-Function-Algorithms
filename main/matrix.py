class matrix():
    def __init__(self, matrix_list: list[list]) -> None:
        self.matrix = matrix_list
        self.row_length = len(self.matrix)
        self.col_length = len(self.matrix[0])
        
        for row in self.matrix:
            try:
                assert len(row) == self.col_length
            except:
                ValueError("All rows must have the same number of columns.")

    def transpose(self):
        return matrix([list(col) for col in zip(*self)])

    def minor(self, pos: tuple[int, int]):
        x, y = pos
        submatrix = []

        for row_idx, row in enumerate(self.matrix):
            if row_idx == x:
                continue

            new_row = []
            for col_idx, elem in enumerate(row):
                if col_idx == y:
                    continue
                new_row.append(elem)

            submatrix.append(new_row)

        return matrix(submatrix)

    def cofactor(self, pos: tuple[int, int]):
        return (-1)**(pos[0] + pos[1]) * self.minor(pos).det()
    
    def det(self):
        self.__check_square()
        if self.row_length == 1:
            return self.matrix[0][0]

        if self.row_length == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        
        total = 0
        for idx, element in enumerate(self.matrix[0]):
            total += element * self.cofactor((0, idx))
        return total

    def __iter__(self):
        for row in self.matrix:
            yield row

    def __len__(self) -> list:
        return [self.row_length, self.col_length]

    def __contains__(self, other) -> bool:
        if not isinstance(other, matrix):
            for row in self.matrix:
                for col in row:
                    if other == col:
                        return True
            
        return False
    
    def __abs__(self) -> 'matrix':
        return matrix([[abs(col) for col in row] for row in self.matrix])

    def __neg__(self) -> 'matrix':
        return matrix([[-col for col in row] for row in self.matrix])

    def __eq__(self, other: 'matrix') -> bool:
        self.__check_other_equal_row_col(other)

        for index, row in enumerate(other):
            if self.matrix[index] != row: 
                return False
        return True

    def __add__(self, other) -> 'matrix':
        if isinstance(other, matrix):
            self.__check_other_equal_row_col(other)
            return matrix([[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self, other)])
        
        elif isinstance(other, (int, float)):
            return matrix([[col + other for col in row] for row in self.matrix])
        
        raise TypeError(f"Unsupported operand type(s) for +: 'matrix' and '{type(other)}'.")
        
    def __radd__(self, other) -> 'matrix':
        return self.__add__(other)

    def __sub__(self, other) -> 'matrix':
        if isinstance(other, matrix):
            self.__check_other_equal_row_col(other)
            return matrix([[a - b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self, other)])
        
        elif isinstance(other, (int, float)):
            return matrix([[col - other for col in row] for row in self.matrix])
        
        raise TypeError(f"Unsupported operand type(s) for -: 'matrix' and '{type(other)}'.")
        
    def __rsub__(self, other) -> 'matrix':
        if isinstance(other, (int, float)):
            return matrix([[other - col for col in row] for row in self.matrix])
        
        raise TypeError(f"Unsupported operand type(s) for -: 'matrix' and '{type(other)}'.")

    def __matmul__(self, other: 'matrix') -> 'matrix':
        if isinstance(other, matrix):
            self.__check_matmultiplicable(other)
            return matrix([[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*other)] for row_a in self.matrix])
        
        raise TypeError(f"Unsupported operand type(s) for @: 'matrix' and '{type(other)}'.")
        
    def __rmatmul__(self, other: 'matrix') -> 'matrix':
        if isinstance(other, matrix):
            return other.__matmul__(self)
        
        raise TypeError(f"Unsupported operand type(s) for @: 'matrix' and '{type(other)}'.")

    def __mul__(self, other):
        if isinstance(other, matrix):
            return self.__matmul__(other)
        
        elif isinstance(other, (int, float)):
            return matrix([[col * other for col in row] for row in self.matrix])
        
        raise TypeError(f"Unsupported operand type(s) for *: 'matrix' and '{type(other)}'.")
    
    def __rmul__(self, other):
        if isinstance(other, matrix):
            return self.__rmatmul__(other)
        
        elif isinstance(other, (int, float)):
            return matrix([[col * other for col in row] for row in self.matrix])
        
        raise TypeError(f"Unsupported operand type(s) for *: 'matrix' and '{type(other)}'.")

    def __repr__(self) -> str:
        return self
    
    def __str__(self) -> str:
        return str(self.matrix)

    def __check_other_equal_row_col(self, other: 'matrix', check_row: bool = True, check_col: bool = True) -> None:
        if check_row:
            try:
                assert self.row_length == other.row_length
            except:
                raise ValueError("Matrices must have the same row length.")
            
        if check_col:
            try:
                assert self.col_length == other.col_length
            except:
                raise ValueError("Matrices must have the same column length.")

    def __check_matmultiplicable(self, other: 'matrix') -> None:
        try:
            assert self.col_length == other.row_length
        except:
            raise ValueError("Matrices must have the same row length.")

    def __check_square(self) -> None:
        try:
            assert self.col_length == self.row_length
        except:
            raise ValueError("Matrix must be a square matrix.")    

class zero_matrix(matrix):
    def __init__(self, rows: int, cols: int):
        matrix_list = [[0] * cols for _ in range(rows)]
        super().__init__(matrix_list = matrix_list)

class identity_matrix(matrix):
    def __init__(self, size: int):
        matrix_list = [[0] * size for _ in range(size)]
        for i in range(size):
            matrix_list[i][i] = 1
        super().__init__(matrix_list = matrix_list)

A = matrix([[-1, 2, 3], [4, 5, 6]])
B = matrix([[-1, 2, 3], [4, 5, 6]])
C = matrix([[-1, 2], [4, 5], [4, 5]])

Z = zero_matrix(2, 1)
I = identity_matrix(2)

print(A == B)
print(A + B)
print(A - 3)
print(3 - A)
print(abs(A))
print(A @ C)
print(C * A)
print(A.transpose())
print(Z)
print(I)
A = matrix([[7, 8], [7, 9]])
B = matrix([[1, 1, 1], [0, 1, -1]])

print(A)
print(B)
print(A*B)
print(A*I)
A = matrix([[777, 81, 25], [7, 9, -97], [74, 4, -4]])
print(A.det())