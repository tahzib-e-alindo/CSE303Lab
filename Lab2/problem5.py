# string = "Practice Problems to Drill List Comprehension in Your Head."
#5. Find all of the words in a string that are less than 5 letters (use string above)
def ListToString(s):
    str = ""
    for e in s:
        str += e + "\n"
    return str
string = "Practice Problems to Drill List Comprehension in Your Head."
string = string.strip(".")
result = [i for i in string.split(" ") if len(i) < 5]
print(ListToString(result))
