     # Q1-> Add 2 Matrices -:

m , n = map(int,input('Enter Matrix structure in M * N : ').split())
print('Enter the element : ')
matrix1 = []

for i in range(m):     # i is row
    row = []
    for j in range(n):   # j is columns
        k = int(input())
        row.append(k)
    matrix1.append(row)

print('Enter the element of second matrix : ')
# matrix2 = [[int(input()) for j in range(n)] for i in range(m)]
matrix2 = []
for i in range(m):
    row = []
    for j in range(n):
        k = int(input())
        row.append(k)
    matrix2.append(row)

major = []
for i in range(m):
    minor = []
    for j in range(n):
        k = matrix1[i][j] + matrix2[i][j]
        minor.append(k)
    major.append(minor)

for minor in major:
    print(minor)
for i in range(m):
    for j in range(n):
        print(major[i][j], end=' ')

    print()