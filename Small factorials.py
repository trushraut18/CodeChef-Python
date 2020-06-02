'''
==============================
Sample input:
==============================
4
1
2
5
3
==============================
Sample output:
==============================
1
2
120
6
==============================
Solution
==============================
'''
def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
cases = int(input())
for cases in range(0,cases):
    n = int(input())
    print(fact(n)
