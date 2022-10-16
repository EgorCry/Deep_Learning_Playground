#Правильное решение

def rotate_90_clockwise(matrix):
    def transpose(a):
        r, c = len(a), len(a[0])
        t = [[None] * r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                t[j][i] = a[i][j]
        return t

    matrix[:] = transpose(matrix)
    for r in range(len(matrix)):
        matrix[r] = matrix[r][::-1]
    return matrix


def main_func(xmpl, rqst, n1, m1):
    i1, i2 = 0, n1
    j1, j2 = 0, m1
    for m in range(4):
        while i2 <= len(rqst):
            while j2 <= len(rqst[0]):
                matrix = []
                check = rqst[i1:i2]
                for i in range(n1):
                    matrix.append(check[i][j1:j2])
                if xmpl == matrix:
                    return True
                j1 += 1
                j2 += 1
            i1 += 1
            i2 += 1
            j1 = 0
            j2 = m1
        i1, i2 = 0, n1
        j1, j2 = 0, m1
        if m != 3:
            rqst = rotate_90_clockwise(rqst)
    return False


n1, m1 = [int(i) for i in input().split()]
xmpl = [[i for i in input()] for _ in range(n1)]
n2, m2 = [int(i) for i in input().split()]
rqst = [[i for i in input()] for _ in range(n2)]


result = main_func(xmpl, rqst, n1, m1)
print('Yes' if result else 'No')