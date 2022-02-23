lst1 = [1,2,3,4,5,6,7,8,9]
lst2 = [11,12,13,14,15,16,17,18,19]
lst3 = [n for n in lst1 if n%2]+[n for n in lst2 if not n%2]
print(lst3)