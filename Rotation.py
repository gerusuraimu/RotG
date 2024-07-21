class RotationFunc:
    def rotation_left(self, matrix: list, repeat: int) -> list:
        repeat: int = repeat if repeat < 4 else repeat - (repeat // 4) * 4
        dimension: int = self.__get_dimension(matrix)
        if 1 < dimension:
            for _ in range(repeat):
                matrix = [list(items) for items in zip(*map(reversed, matrix))]
        return matrix

    def rotation_right(self, matrix: list, repeat: int) -> list:
        repeat: int = repeat if repeat < 4 else repeat - (repeat // 4) * 4
        dimension: int = self.__get_dimension(matrix)
        if 1 < dimension:
            for _ in range(repeat):
                matrix = [list(reversed(items)) for items in zip(*matrix)]
        return matrix

    def __get_dimension(self, matrix: list, n: int = 0) -> int:
        if not matrix:
            return n
        if matrix and isinstance(matrix[0], list):
            return self.__get_dimension(matrix[0], n + 1)
        else:
            return n + 1


class MatrixRotation(RotationFunc):
    def left(self, matrix: list, repeat: int) -> list: return self.rotation_left(matrix, repeat)
    def right(self, matrix: list, repeat: int) -> list: return self.rotation_right(matrix, repeat)
    def left90(self, matrix: list) -> list: return self.rotation_left(matrix, 1)
    def left180(self, matrix: list) -> list: return self.rotation_left(matrix, 2)
    def left270(self, matrix: list) -> list: return self.rotation_left(matrix, 3)
    def right90(self, matrix: list) -> list: return self.rotation_right(matrix, 1)
    def right180(self, matrix: list) -> list: return self.rotation_right(matrix, 2)
    def right270(self, matrix: list) -> list: return self.rotation_right(matrix, 3)
