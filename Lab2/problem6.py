# string = "Practice Problems to Drill List Comprehension in Your Head."
#6. Use a dictionary comprehension to count the length of each word in a sentence (use string above)

string = "Practice Problems to Drill List Comprehension in Your Head."
string = string.strip(".")
word_len = {w:len(w) for w in string.split(" ")}
print(word_len)