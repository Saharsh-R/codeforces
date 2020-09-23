"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""

if __name__== "__main__":
    # Write your solution here
    n = int(input())
    points = {}
    for _ in range(n):
        x,y = [int(x) for x in input()]
        points.add((x,y))
    maxdist = float('-inf')

