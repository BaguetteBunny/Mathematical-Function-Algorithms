class matrix():
    def __init__(self, matrix_list: list[list]):
        self.matrix = matrix_list
        self.row_length = len(self.matrix[0])
        self.col_length = len(self.matrix)

        for row in self.matrix:
            assert len(row) == self.row_length

    def __iter__(self):
        for row in self.matrix:
            yield row

    def __eq__(self, other: 'matrix'):
        self.__check_other_type_at_operation(other, '==')
        for index, row in enumerate(other):
            if self.matrix[index] == row: continue
            else: return False

        return True
    
    def __add__(self, other: 'matrix'):
        self.__check_other_type_at_operation(other, '+')
        self.__check_other_equal_row_col(other)

        new_matrix_list = []
        for row_index, row in enumerate(other):
            new_matrix_row_list = []
            for col_index, col in enumerate(row):
                new_matrix_row_list.append(self.matrix[row_index][col_index] + col)
            new_matrix_list.append(new_matrix_row_list)
        return matrix(new_matrix_list)
    
    def __repr__(self):
        final_string = ""
        for row in self.matrix:
            final_string += f"{row}\n"

        return final_string
    
    def __check_other_type_at_operation(self, other: 'matrix', operator: str):
        try:
            assert isinstance(other, matrix)
        except:
            raise TypeError(f"Unsupported operand type(s) for {operator}: 'matrix' and '{type(other)}'")
        
    def __check_other_equal_row_col(self, other: 'matrix', check_row: bool = True, check_col: bool = True):
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


A = matrix([[1, 2, 3], [4, 5, 6]])
B = matrix([[1, 2, 3], [4, 5, 6]])
print(A + B)