"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or m steps. In how many distinct ways can you
climb to the top?
Example 1
Input: n = 2, m = 2
Output: 2
Explanation: 1 step + 1 step; 2 steps
Example 2
Input: n = 6, m = 3
Output: 6
"""


def climb_stairs_m(n, m):
    nswr = [1] * m
    
    for i in range(n - m + 1):
        temp = nswr.copy()
        nswr[0] = nswr[0] + nswr[m-1]
        for j in range(1, m):
            nswr[j] = temp[j-1]
    
    return nswr[0]


print(climb_stairs_m(2, 2))
print(climb_stairs_m(3, 2))
print(climb_stairs_m(6, 3))
print(climb_stairs_m(6, 4))
