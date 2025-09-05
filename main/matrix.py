class matrix():
    def __init__(self, matrix_list: list[list]):
        self.matrix = matrix_list
        self.row_length = len(self.matrix[0])
        self.col_length = len(self.matrix)

        for row in self.matrix:
            assert len(row) == self.row_length

    def __repr__(self):
        final_string = ""
        for row in self.matrix:
            final_string += f"{row}\n"
        return final_string


a = matrix([[1, 2, 3], [4, 5, 6]])
print(a)