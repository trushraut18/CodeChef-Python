'''
=============================
Input
=============================
3 
1 2
100 200
40 15
=============================
Output
1
100
10
=============================
Solution
=============================
'''
cases= int(input())
for cases in range(0,cases):
    n1,n2 = map(int,input().split())
    print(n1%n2)
    
