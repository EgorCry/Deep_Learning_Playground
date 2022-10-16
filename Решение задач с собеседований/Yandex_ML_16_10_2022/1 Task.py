def rotate_180(matrix):
    matrix = rotate_90_clockwise(matrix)
    nswr = rotate_90_clockwise(matrix)
    return nswr


def rotate_90_clockwise(matrix):
    m = len(matrix)
    n = len(matrix[0])
    nswr = [[''] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            nswr[j][m-i-1] = matrix[i][j]
    return nswr


def rotate_90_counterclockwise(matrix):
    nswr = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1, -1, -1)]
    return nswr


# n1, m1 = [int(i) for i in input().split()]
# xmpl = [[i for i in input()] for _ in range(n1)]
# n2, m2 = [int(i) for i in input().split()]
# rqst = [[i for i in input()] for _ in range(n2)]

xmpl = [[1, 2, 3], [4, 5, 6]]
rqst = [[6, 5, 4], [3, 2, 1]]
n1, m1, n2, m2 = 2, 3, 2, 3

if n1 == n2 and m1 == m2:
    if rqst == xmpl:
        print('Yes1')
    elif rotate_180(rqst) == xmpl:
        print('Yes2')
    else:
        print('No')
else:
    check_rqst_clockwise = rotate_90_clockwise(rqst)
    if check_rqst_clockwise == xmpl:
        print('Yes3')
    else:
        check_rqst_counterclockwise = rotate_90_counterclockwise(rqst)
        if check_rqst_counterclockwise == xmpl:
            print('Yes4')
        else:
            print('No')
