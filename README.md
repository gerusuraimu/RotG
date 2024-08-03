# 置き場所
以下のコマンドでmain.py(またはそれに準ずるpythonファイル)と同じディレクトリに置いてください。
```
git clone https://github.com/gerusuraimu/RotG.git
```

# import
```
from RotG import MatrixRotation as Rot


def main():
    rot = Rot()  # インスタンス化
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print(rot)  # 簡単な使い方説明が出力される。

    rotated_right_matrix = rot.right90(matrix)  # 右に90度回転させる。


if __name__ == '__main__':
    main()
```

# 機能一覧
```
from RotG import MatrixRotation as Rot


def main():
    rot = Rot()
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    # 以下、回転機能一覧
    rotated_right_matrix = rot.left(matrix, repeat=2)
    rotated_right_matrix = rot.left90(matrix)
    rotated_right_matrix = rot.left180(matrix)
    rotated_right_matrix = rot.left270(matrix)
    rotated_right_matrix = rot.right(matrix, repeat=3)
    rotated_right_matrix = rot.right90(matrix)
    rotated_right_matrix = rot.right180(matrix)
    rotated_right_matrix = rot.right270(matrix)


if __name__ == '__main__':
    main()
```
