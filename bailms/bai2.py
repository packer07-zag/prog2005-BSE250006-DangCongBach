a,b=map(float,input().split())

mua,mub=a**2,b**2
cana,canb=a**0.5,b**0.5
chianguyen=int(a//b)
chiadu=int(a%b)
lamtrona=round(a)
lamtronb=round(b)

print(f"a^2 = {mua:.2f}")
print(f"b^2 = {mub:.2f}")
print(f"cana(a) = {cana:.2f}")
print(f"canb(b) = {canb:.2f}")
print(f"a//b = {chianguyen}")
print(f"a%b = {chiadu}")
print(f"lamtron(a) = {lamtrona}")
print(f"lamtron(b) = {lamtronb}")