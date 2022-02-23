def palindrome_check_2019_3_60_018(str):
    length = len(str)
    i = 0
    while i<length//2:
        if str[i] != str[length-1-i]:
            return False
        i = i+1
        return True


string = input("enter the string: ")

if palindrome_check_2019_3_60_018(string):
    print("Palindrome")
else:
    print("Not Palindrome")
