# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for _ in range(n):
    s=input()
    odd=""
    even=""
    for i in range(len(s)):
        if i%2==0:
            odd+=s[i]
        else:
            even+=s[i]
                            
    print(odd,even)
                                