#! python3
"""
Have the user enter a number.
Display the multiples of that number, up to 12 times that number:
All numbers should be on the same line.
You may need to use the:
print( variable , end='') option to print on one line
(2 marks)

inputs:
int number

outputs:
multiples of that number on one line

example:
Enter a number: 4
4 8 12 16 20 24 28 32 36 40 44 48
"""
x=int(input("enter a intager=>"))
y=1
e=0
num=True
while num:
    r=x*y
    print(f"{r}" , end = ' ')
    y=y+1
    e=e+1
    if e==12:
        num=False