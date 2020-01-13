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
    def create_diagonal(x,m,n):
        x=matrix.create1(x,x)
        for i in range(len(x)):
            x[i][i]=random.randrange(m,n+1)
        return x

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
    def transpose(mat):
        mt=matrix.create1(len(mat[0]),len(mat))
        for i in range(len(mat)):
            for k in range(len(mat[i])):
                mt[k][i]=mat[i][k]
        return mt
    @staticmethod
    def compare(matrix1,matrix2):
        height=True if len(matrix1) == len(matrix2) else False
        lenght=True if len(matrix1[0]) == len(matrix2[0]) else False
        matrix_same=True
        if height and lenght:
            for i in range(len(matrix1)):
                for j in range(len(matrix1[i])):
                    if matrix1[i][j] == matrix2[i][j]:
                        pass
                    else:
                        matrix_same=False
                        return matrix_same
        else:
            return  True if height and lenght else False
        return matrix_same
                    


m = matrix.create1(4,3)
matrix.print(m)
a = matrix.create1(4,3)
matrix.print(a)
z = matrix.create_unit(4)
print(matrix.compare(m,z))

#matrix.print(z)
#k = matrix.create1(3,5)
#k=matrix.fill_rand(k,1,9)
#matrix.print(k)
#print()
#k=matrix.transpose(k)
#matrix.print(k)
#x=matrix.create_diagonal(3,10,50)
#matrix.print(x)