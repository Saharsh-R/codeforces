"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""

if __name__== "__main__":
    # Write your solution here
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    arr[0::2], arr[1::2]= arr[n//2:], arr[:n//2]
    # if n%2==1:
    #     print(n//2)
    #     print(*arr)
    # else:
    #     print((n-1)//2)
    #     print(*arr)
    ans = 0
    for i in range(1, n-1):
        if arr[i]<arr[i-1] and arr[i]<arr[i+1]:
            ans+=1
    print(ans)
    print(*arr)

