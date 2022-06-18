'''
X= [
       0 [10,200,300],
       1 [45 ,55,6],
       2 [7 ,8,99]
    ]
 
Y = [
        [91,8,7],
        [67,52,4],
        [3,26,1]
    ]

z = [
        [21,8,7],
        [67,82,4],
        [32,46,1]
    ]
'''


'''

result = 
    [[x+y+z,x+y+z,x+y+z],
    [x+y+z ,x+y+z,x+y+z],
    [x+y+z ,x+y+z,x+y+z]]
'''
def matrix_addition(x, y, z):
    matrix_addition = []
    for i in range(len(x)):
        a = [0]*3
        for j in range(len(x[0])):
            a[j] = x[i][j]+ y[i][j]+z[i][j]
        matrix_addition.append(a)
    return matrix_addition

x = [
        [10,200,300], 
        [45 ,55,6], 
        [7 ,8,99]
    ]
y = [
        [91,8,7],
        [67,52,4],
        [3,26,1]
    ]
z = [
        [21,8,7],
        [67,82,4],
        [32,46,1]
    ]

result = matrix_addition(x, y, z)
print(result)

