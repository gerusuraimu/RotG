from RotG import Rotation


def printer(func):
    def wrapper(*args, **kwargs):
        print('---------')
        func(*args, **kwargs)
    return wrapper


@printer
def return_print(matrix):
    print(*matrix, sep='\n')


def demo():
    rot = Rotation()
    matrix_2d = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]

    return_print(matrix_2d)
    return_print(rot.left90(matrix_2d))
    return_print(rot.left180(matrix_2d))
    return_print(rot.left270(matrix_2d))
    return_print(rot.right90(matrix_2d))
    return_print(rot.right180(matrix_2d))
    return_print(rot.right270(matrix_2d))
    return_print(rot.left(matrix_2d, repeat=10000000000001))
    return_print(rot.right(matrix_2d, repeat=10000000000001))


if __name__ == '__main__':
    demo()
