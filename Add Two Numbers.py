'''
Input
3 
1 2
100 200
10 40

Output
3
300
50
'''
'''
==========================
Solution
==========================
'''
T = int(input())
for tc in range(T):
	(a, b) = map(int, input().split(' '))
	ans = a + b
	print(ans)
