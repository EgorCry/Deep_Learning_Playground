"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
Example 1
Input: n = 2
Output: 2
Explanation: 1 step + 1 step; 2 steps
Example 2
Input: n = 3
Output: 3
Explanation: 1 step + 1 step + 1 step; 1 step + 2 steps; 2 steps + 1 step
"""


def climb_stairs(n):
    one, two = 1, 1
    
    for i in range(n - 1):
        one, two = one + two, one
    
    return one


print(climb_stairs(5), end='\n\n')

for i in range(1, 11):
    print(climb_stairs(i))
