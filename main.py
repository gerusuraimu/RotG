from RotG import Rotation


def printer(func):
    def wrapper(*args, **kwargs):
        print('---------')
        func(*args, **kwargs)
    return wrapper


@printer
def return_print(matrix):
    print(*matrix, sep='\n')


def main():
    rot = Rotation()
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    return_print(matrix)
    return_print(rot.left90(matrix))
    return_print(rot.left180(matrix))
    return_print(rot.left270(matrix))
    return_print(rot.right90(matrix))
    return_print(rot.right180(matrix))
    return_print(rot.right270(matrix))
    return_print(rot.left(matrix, repeat=10000000000001))
    return_print(rot.right(matrix, repeat=10000000000001))


if __name__ == '__main__':
    main()
