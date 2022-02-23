def EvenSum(a, n):
    result = 0
    for i in range(n):
        if i % 2 == 0:
            result += a[i]
    print("Even index positions sum ", result)

lst = [11, 23, 35, 47, 60]
n = len(lst)

EvenSum(lst, n)