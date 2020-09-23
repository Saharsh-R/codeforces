"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""

if __name__== "__main__":
    # Write your solution here
    t = int(input())
    for  _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        lock = [int(x) for x in input().split()]
        sortthis = [a for a,b in zip(arr , lock) if not b]
        sortthis.sort(reverse=1)
        indexs = [i for i,x in enumerate(lock) if x==0]
        for i,x in zip(indexs, sortthis):
            arr[i]=x
        print(*arr)
