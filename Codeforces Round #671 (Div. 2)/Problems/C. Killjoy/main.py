"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""

if __name__== "__main__":
    # Write your solution here
    t = int(input())
    for i in range(t):
        n,k = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]
        inc = 0
        dec = 0
        one = False
        for x in arr:
            aux = x-k
            if aux==0:
                one = True
            elif aux<0:
                inc -=aux
            elif aux>0:
                dec+=aux
        if inc ==dec==0:
            print(0)
        elif inc==dec or one:
            print(1)
        else:
            print(2)



