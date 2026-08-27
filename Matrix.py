     # Q1-> Add 2 Matrices -:

# m , n = map(int,input('Enter Matrix structure in M * N : ').split())
# print('Enter the element : ')
# matrix1 = []
#
# for i in range(m):     # i is row
#     row = []
#     for j in range(n):   # j is columns
#         k = int(input())
#         row.append(k)
#     matrix1.append(row)
#
# print('Enter the element of second matrix : ')
# # matrix2 = [[int(input()) for j in range(n)] for i in range(m)]
# matrix2 = []
# for i in range(m):
#     row = []
#     for j in range(n):
#         k = int(input())
#         row.append(k)
#     matrix2.append(row)
#
# major = []
# for i in range(m):
#     minor = []
#     for j in range(n):
#         k = matrix1[i][j] + matrix2[i][j]
#         minor.append(k)
#     major.append(minor)
#
# for minor in major:
#     print(minor)
# for i in range(m):
#     for j in range(n):
#         print(major[i][j], end=' ')
#
#     print()


    # Q2-> Transpose a Matrix -:

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9,]
#           ]
#
# transport = []
# for i in range(len(matrix[0])):
#     row = []
#     for j in range(len(matrix)):
#         row.append(matrix[j][i])
#     transport.append(row)
#
# print('transport Matrix : ')
# for row in transport:
#     print(row)
#



     # Q3-> Multiply two matrices -:

matrix1  = [[1,2,3],
          [4,5,6],
          [3,4,5]
          ]
matrix2 = [[2,3,4],
           [4,5,3],
           [9,8,3]
           ]


mul = []
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix2[0])):
        row .append(0)
    mul.append(row)



for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            mul[i][j] = mul[i][j] +matrix1[i][k] * matrix2[k][j]
for row in mul:
    print(row)


