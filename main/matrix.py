class matrix():
    def __init__(self, matrix_list: list[list]) -> None:
        self.matrix = matrix_list
        self.row_length = len(self.matrix[0])
        self.col_length = len(self.matrix)

        for row in self.matrix:
            assert len(row) == self.row_length

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
        
    def __repr__(self) -> str:
        final_string = ""
        for row in self.matrix:
            final_string += f"{row}\n"

        return final_string

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



A = matrix([[-1, 2, 3], [4, 5, 6]])
B = matrix([[-1, 2, 3], [4, 5, 6]])
C = matrix([[-1, 2], [4, 5], [4, 5]])

print(A == B)
print(A + B)
print(A - 3)
print(3 - A)
print(abs(A))
print(A @ C)