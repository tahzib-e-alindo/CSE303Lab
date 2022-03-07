# string = "Practice Problems to Drill List Comprehension in Your Head."
#4. Remove all of the vowels in a string (use string above)
def ListToString(s):
    str = ""
    for e in s:
        str += e
    return str

string = "Practice Problems to Drill List Comprehension in Your Head."
vowels = ['a','e','i','o','u']
result = [i for i in string if i not in vowels]
print((ListToString(result)))