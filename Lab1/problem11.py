str = input("Enter the string:")

for i in range(len(str)):
    if i % 2 == 0:
        print(str[i], end='')