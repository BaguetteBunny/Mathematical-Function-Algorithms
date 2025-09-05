class matrix():
    def __init__(self, matrix_list: list[list]):
        self.matrix = matrix_list
        self.row_length = len(self.matrix[0])
        self.col_length = len(self.matrix)

        for row in self.matrix:
            assert len(row) == self.row_length

    def __eq__(self, other):
        assert isinstance(other, matrix)
        for index, row in enumerate(other):
            if self.matrix[index] == row: continue
            else: return False

        return True
    
    def __iter__(self):
        for row in self.matrix:
            yield row

    def __repr__(self):
        final_string = ""
        for row in self.matrix:
            final_string += f"{row}\n"

        return final_string


A = matrix([[1, 2, 3], [4, 5, 6]])
B = matrix([[1, 2, 3], [4, 5, 6]])
print(A == B)