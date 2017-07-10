class Matrix:
    @staticmethod
    def transpose(matrix):
        return list(zip(*matrix))
    @staticmethod
    def column(matrix, i):
        return [row[i] for row in matrix]
    @staticmethod
    def dump(matrix):
        print('\n'.join([' : '.join(['{:4}'.format(item) for item in row]) for row in matrix]))