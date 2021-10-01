#! python3

"""
Count by 2's and display all the numbers, 1 on each line.
Continue until the current value is 20
You will need to keep track of a current value, and modify
or update the current value through every iteration of the
while loop

(2 marks)
Inputs:
none

Outputs:
Example:
2
4
6
8
10
...
"""
e=2
print(f"{e}" , end = ' ')
num=True
while num:
    e=e+2
    print(f"{e}" , end = ' ')
    if e==20:
        num=False