# string = "Practice Problems to Drill List Comprehension in Your Head."
#3. Count the number of spaces in a string (use string above)

string = "Practice Problems to Drill List Comprehension in Your Head."
result = [i for i in string if i == " "]
print(len(result))
