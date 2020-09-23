"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""
import  bisect
if __name__== "__main__":
    # Write your solution here
    t = int(input())
    numb = [1]
    cost = [1]
    while cost[-1]<10**19:
        numb.append(numb[-1]*2 + 1)
        cost.append(cost[-1] + numb[-1]*(numb[-1]+1)//2)

    for _ in range(t):
        n = int(input())
        print(bisect.bisect_right(cost, n))


