str = input("Enter the string:")
str1 = 'CSE303'
count = 0
str1_len = len(str1)
for i in range(len(str)):
    if str[i:i+str1_len] == str1:
        count += 1
print(count)