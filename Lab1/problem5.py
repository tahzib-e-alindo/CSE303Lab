from math import sqrt


def prime_find_2019_3_60_018(n):
    if (n <= 1):
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            return False

    return True


if prime_find_2019_3_60_018(int(input("Enter value:"))):
    print("Prime Number")
else:
    print("Not Prime Number")