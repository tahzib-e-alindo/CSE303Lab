#8. For all the numbers 1–1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by.
max_nums = { i: max([j for j in range(1,10) if i % j == 0]) for i in range(1,1001)}
print(max_nums)