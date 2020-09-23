"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""

if __name__== "__main__":
    # Write your solution here

    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        odd = 0
        even = 0
        if n%2==0:
            if any(int(x)%2==0 for x in s[1::2]):
                print(2)
            else:
                print(1)
        else:
            if any(int(x)%2==1 for x in s[0::2]):
                print(1)
            else:
                print(2)

