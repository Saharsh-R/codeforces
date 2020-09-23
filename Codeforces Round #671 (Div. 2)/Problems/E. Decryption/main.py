"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""
import math
if __name__== "__main__":
    # Write your solution here
    def find(n):
        ans = []
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                power = 0
                while n%i==0:
                    power += 1
                    n//=i
                ans.append((i,power))
        if n!=1:
            ans.append((n,1))

        return ans

    t = int(input())
    for _ in range(t):
        n = int(input())

        facts = find(n)

        output = []
        def back(i, parent, expo=None):
            if parent:
                expo = [0]*(len(facts))
            if i==len(facts):
                curr = 1
                for i,x in enumerate(expo):
                    curr*= facts[i][0]**x
                output.append(curr)
                return
            else:
                for exp in range(parent, facts[i][1]+1):
                    expo[i]=exp
                    back(i+1, 0,expo)
        for i in range(len(facts)):
            back(i, 1)


        for i in range(len(output)):
            if output[i]%facts[-1][0]==0:
                new = output[i]
                del output[i]
                output = [new]+output
                break
        print(*output)
        if len(output)==3 and len(facts)==2:
            print(1)
        else:
            print(0)




