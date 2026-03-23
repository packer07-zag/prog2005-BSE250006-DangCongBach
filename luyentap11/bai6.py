d={}
n=int(input())

for i in range(n):
    ten=input()
    tuoi=int(input())
    d[ten]=tuoi

s=0
for i in d.values():
    s+=i

print("Tuoi tb:",s/n)