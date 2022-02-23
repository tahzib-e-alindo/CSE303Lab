def largest_number_2019_3_60_018(a, n):
    max = a[0]
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    print("largest element in the list is ", max)


def smallest_number_2019_3_60_018(a, n):
    min = a[0]
    for i in range(len(a)):
        if a[i] < min:
            min = a[i]
    print("smallest element in the list is ", min)


lst = [11, 23, 35, 47, 59]
c = len(lst)
largest_number_2019_3_60_018(lst, c)
smallest_number_2019_3_60_018(lst, c)