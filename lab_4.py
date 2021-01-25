
# Problem 1:
def count_evens(L):
    # returns the number of even integers in the list, L
    counter = 0
    for i in L:
        if i % 2 == 0:
            counter += 1

    return counter

print(count_evens([22,42,2,23,55]))


# Problem 2:
def list_to_str(lis):
    temp = "["
    for j in range(len(lis)):
        temp = temp + str(lis[j])
        if (j != len(lis) - 1):
            temp += ", "
    temp += "]"
    return temp

print(list_to_str([1,2,3]))

# Problem 3:
def lists_are_the_same(list1, list2):
    """Compare two lists"""

    # first check that both lists are of the same size
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True 
    else:
        return False

print(lists_are_the_same([1,2,3],[1,2,3]))

# Problem 4: Simplifying Fractions:
def simplify_fraction(n, m):
    # Print the simplified version of the fraction n/m
    if n > m:
        # finds the greatest common factor and divides first 
        for i in range(n, 1, -1):
            if n % i == 0 and m % i == 0:
                n /= i
                m /= i
                break
    else:
        for j in range(m, 1, -1):
            if n % j == 0 and m % j == 0:
                n /= j
                m /= j
                break
    return (f"{int(n)}/{int(m)}")


print(simplify_fraction(4, 16))



#Problem 5:

import math
def sum_more_pi(n):
    """
    Return the number of terms needed to be added in the
    summation to approximate pi to n significant digits.
    """
    x = math.pi
    pi = int(x*(10**(n-1)))

    k, pi_approx, final_sum = 0, 0, 0

    while pi != pi_approx:
        if (k % 2 == 0):
            numerator = 1
        else:
            numerator = -1
        final_sum += numerator/(2 * k + 1)
        pi_approx = int((4 * final_sum)*(10**(n-1)))

        k += 1 

    return k

print(sum_more_pi(2))




# Problem 6:

def euclid(a, b):
    """Returns the GCF"""
    x = min(a, b)
    y = max(a, b)
    if (x != 0):
        return(euclid(x, y%x))
    else:
        return y

def simplify_frac(a, b):
    y = euclid(a,b)
    return f"{int(a/y)}/{int(b/y)}"

print(simplify_frac(80,40))

