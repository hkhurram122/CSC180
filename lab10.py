# RECURSION


# Problem 1


def power(x, n):
    """Returns x^n, assuming n is a non-negative integer"""
    # base case:
    if n == 1:
        return x 
    # recursive case
    return x * power(x, n-1)

print(power(2,5))



# Problem 2

def interleave(L1, L2):
    """Takes in 2 lists of the same length, and 
    returns a list which consists of L1 and L2 
    interleaved."""
    if len(L1) == 0:
        return []
    return [L1[0], L2[0]] + interleave(L1[1:], L2[1:])

r = interleave([4,4,4,4,4], [5,5,5,5,5])


print(r)



# Problem 3:

def reverse_rec(L):
    """Function that reverses a list in place"""
    if len(L) == 0:
        return []
    else:
        return [L.pop()] + reverse_rec(L)

# binary reverse (runtime == O(log n))?

print(reverse_rec([1,2,4,6,7,8,9]))




# Problem 4

def zigzag1(L):
    if len(L) == 0:
        print('')
    elif len(L) == 1:
        print(L[0], end = " ")
    else:
        print(L[0], L[-1], end = " ") 
        zigzag1(L[1:-1])

L = [1,2,4,6,7,8]
zigzag1(L)
# assume n is odd (len(L))



L = [1,2,4,6,7,8]

def zigzag2(L):
    if len(L) == 0:
        print('')
    elif len(L) == 1:
        print(L[len(L) // 2], end = " ")
    else:
        print(L[len(L)//2],L[len(L)//2 - 1], end = " ")
        zigzag2(L[0:len(L)//2 - 1] + L[len(L)//2 + 1:])
zigzag2(L)


# Problem 5


# symmetry questions with recursion


def is_balanced1(s):
    # may use str.find()
    # loop from start to end 
    # loop from end to start


    close = s.find(")")
    if "(" not in s and close != -1:
        return False
    openn = s[:close].find("(")
    if ")" not in s and openn != -1:
        return False

    if close == openn == -1:
        return True

    is_balanced1(s[:open] + s[close+1:])




def is_balanced2(s):
    """Checking for balanced paranthesis"""

    # find a matching pair of balanced paranthesis
    # then remove the innermost pair 
    
    end = s.find(')') # find the first closing parenthesis

    if end == -1: # find returns -1
        return '(' not in s

    # for it so be balanced, if theres no )
    # then theres got to be no (

    

    # str.rfind is the same as str.find, except it 
    # looks from right to left 

    start = s[:end].rfind('(')

    # is there an open paranthesis
    #found a 
    if start == -1: # then return False
        return False 
        # have a closing paranthesis, NO
        # opening paranthesis

    # remove the matching pair and everything in between

    ss = s[:start] + s[end+1:]
    return is_balanced2(ss)



print(is_balanced2("(())())"))
