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

    def __eq__(self, other):
        assert isinstance(other, matrix)
        for index, row in enumerate(other):
            if self.matrix[index] == row: continue
            else: return False

        return True
    
    def __add__(self, other):
        assert isinstance(other, matrix)
        assert self.row_length == other.row_length
        assert self.col_length == other.col_length

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


A = matrix([[1, 2, 3], [4, 5, 6]])
B = matrix([[1, 2, 3], [4, 5, 6]])
print(A + B)