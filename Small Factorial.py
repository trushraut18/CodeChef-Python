'''
===============================
Input
===============================
3 
3 
4
5
===============================
Output
===============================
6
24
120
===============================
Solution
===============================
def fact(n):
    if n<=1:
        return 1
    else:
       return n*fact(n-1)

cases =int(input())       
for cases in range(0,cases):
    n = int(input())
    print(fact(n))  
