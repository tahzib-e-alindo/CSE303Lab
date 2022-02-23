str = input("Input the string:")
str1 = ""
n = int(input("Enter n value:"))
for i in range(len(str)):
    if i > n:
        str1 = str1 + str[i]
print("The string after removal of characters : " + str1)