#! python3
"""
The Fibonacci sequence was created to model how populations
of bunnies increase over time.  It is also used in strategies
that prolong how long you can play Blackjack before you 
eventually lose all your money.
It follows a pattern where the last two number are added 
together to make the next number, starting with 1 1:
Create a program to show the Fibonacci sequence, stopping
after the number in the sequence is greater than 100:
(2 points) 

Example:
1 1 2 3 5 ...
"""
k=0
x=1
y=1
e= x + y
print(f"{x} {y}" , end = ' ') 
y= e 
d= e
print(f"{y}" , end = ' ')
num=True
while num:
    e= x + y
    y = e
    x = d 
    d = e
    print(f"{y}" , end = ' ')
    k= k+1
    if k==9:
        num=False