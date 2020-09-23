"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""
from itertools import groupby
if __name__== "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ans = 0
        if arr[0]==1:
            ans+=1
        for a,b in groupby(arr[1:]):
            if a==1:
                ans+= len(list(b))//3
        print(ans)





