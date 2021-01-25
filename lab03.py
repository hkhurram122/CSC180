import math
import time


# Problem 2:

def sum_cubes(n):
    temp = 0
    for i in range(1, n + 1):
        temp += i**3
    return temp

def sum_formula(n):
    temp_1 = 0
    for j in range(1, n + 1):
        temp_1 += j
    temp_2 = temp_1 ** 2
    return temp_2

def check_sum(n):
    if (sum_cubes(n) == sum_formula(n)):
        return True
    else:
        return False


def check_sums_up_to_n(N):
    count = 0
    for k in range(1, N+1):
        if check_sum(k) == True:
            count += 1
    if (count == N):
        return True
    else:
        return False


# Problem 2: Sums of Cubes

def compute_sum(n):
    sum_1 = 0
    for i in range(1,n+1):
        sum_1 += i**3
    return sum_1


# Computing the sum using the formula
def sum_formula1(n):
    sum_0 = ((n**2)*((n+1)**2))/ 4
    return sum_0


def check_sum1(n):
    sum_1 = compute_sum(n)
    sum_2 = sum_formula1(n)

    if sum_1 == sum_2:
        return True
    else:
        return False


def check_sums_up_to_n1(N):
    """Return True iff for every n ≤ N, the formula works"""
    for i in range(1,N+1):
        if not check_sum1(i):
            return False
    return True


# Problem 3:

n = 10000
final_sum = 0

for a in range(n+1):
    if (a % 2 == 0):
        numerator = 1
    else:
        numerator = -1
    denominator = 2*a + 1
    term = numerator/denominator
    final_sum += term
pi_approx = 4 * final_sum
print(pi_approx)


def leibniz_sum(k):
    final_sum = 0
    for a in range(k+1):
        if (a % 2 == 0):
            numerator = 1
        else:
            numerator = -1
        denominator = 2*a + 1
        term = numerator/denominator
        final_sum += term
    return (4 * final_sum)


def leibniz_sum(k):
    final_sum = 0
    for a in range(k+1):
        if (a % 2 == 0):
            numerator = 1
        else:
            numerator = -1
        denominator = 2*a + 1
        term = numerator/denominator
        final_sum += term
    return (4 * final_sum)


def sum_more_pi(n):
    """
    Returns the number of terms needed to be added in the
    summation to approximate pi to n significant digits.
    """
    
    x = math.pi
    pi = int(x*(10**(n-1)))
    print(pi)

    k = 0
    pi_approx = 0

    while pi != pi_approx:
        pi_approx = leibniz_sum(k)
        pi_approx = int(pi_approx*(10**(n-1)))
        print(pi_approx)
        k += 1 
        print(k)
        
    return k
