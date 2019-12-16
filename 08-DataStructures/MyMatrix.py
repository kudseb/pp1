import random
class matrix():

    @staticmethod
    def create(x,y):
        matrix = []
        value = 0
        for i in range(x):
            # create single row
            row = []
            for j in range(y):
                row.append(value)
            # add row to matrix
            matrix.append(row)
        return matrix
    
    @staticmethod
    def create1(x,y):
        m=[[0 for y in range(y)] for x in range(x)]
        return m

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
    @staticmethod
    def create_unit(x):
        m=matrix.create1(x,x)
        for i in range(x):
            m[i][i]=1
        return m
    @staticmethod
    def fill_rand(matrix,m,n):
        for i in range(len(matrix)):
            for k in range(len(matrix[i])):
                matrix[i][k]=random.randrange(m,n+1)
        return matrix
    @staticmethod
    def transpose(matrix):
        mt=[]
        for i in range(len(matrix)):
            for k in range(len(matrix[i])):
                mt[k].append([])
    
                mt[k][i]=matrix[i][k]
        return mt


#m = matrix.create1(4,3)
#matrix.print(m)
#z = matrix.create_unit(4)
#matrix.print(z)
k = matrix.create1(3,5)
#matrix.print(k)
k=matrix.fill_rand(k,5,9)
k=matrix.transpose(k)
matrix.print(k)