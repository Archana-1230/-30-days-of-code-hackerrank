# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
d={}
for i in range(n):
    name,phoneno=input().split()
    d[name]=phoneno
try:
    while True:
        x=input()
        if x in d:
            print(f"{x}={d[x]}")
        else:
            print("Not found")
except EOFError:
    pass
    
