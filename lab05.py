# problem 1:



'''
def list1_start_with_list2(list1, list2):

    if len(list1) >= len(list2):
        for i in range(len(list2)):
            if list1[i] != list2[i]:
                return False    

        return True 


'''
# problem 2

def match_pattern(list1, list2):
    for i in range(len(list1)):
        ls = list1[i:i+len(list2)]
        if list2 == ls:
            return True
        
    return False

list1 = [4, 10, 2, 3, 50, 100]
list2 = [2, 3, 50]
print(match_pattern(list1, list2))



# problem 3 

def repeats(list0):
    for i in range(1, len(list0)):
        if list0[i] == list0[i-1]:
            return True 

    return False

print(repeats([1,2,2,2,3,4,5,6,8]))




# problem 4 

# 4a
def print_matrix_dim(M):
    """Print the matrix dimensions"""
    print(f"{len(M)}x{len(M[0])}")
M = ([[1,2],[3,4],[5,6]])
print_matrix_dim(M)


# 4b

def mult_M_v(M,v):

    # number of rows equals the number of columns
    if (len(M[0])) == (len(v)):
        n = [0]*len(v)

        for i in range(len(M)):
            sum = 0 
            for j in range(len(M[0])):
                sum += M[i][j]*v[i]

            n[i] = sum

    return n
    
print(mult_M_v([[1,2,3],[4,3,4],[1,1,1]], [1,1,1]))





def matrix_mult(m1,m2):
    l1, M3 = [], []
    # number of rows of first equals number of cols of second
    if len(m1[0]) == len(m2):
        # loop through rows of M1
        for i in range(len(m1)):
        # loop through columns of M2
            for j in range(len(m2[0])):
                sums = 0
                # loop through rows
                for k in range(len(m2)):
                    sums += m1[i][k] * m2[k][j]
                l1.append(sums)
            M3.append(l1)
            l1 = []
        return M3



# Write a function that deals with addresses in python




            
M = [[1, 1], [21, 21]]
v = [[1,1],[-1,-1]]
print(matrix_mult(M, v))


