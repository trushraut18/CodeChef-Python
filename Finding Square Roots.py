'''
==============================
Input:
==============================
3
10
5
10000
==============================
Output:
==============================
3
2
100
==============================
Solution
==============================
'''
import math
cases = int(input())
for cases in range(0,cases):
    n = int(input())
    print(math.floor(math.sqrt(n)))  
    
