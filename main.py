m =int(input())
n = m
i=0
while (n):
    n =n>>1
    i = (i<<1) |1
out = (~m)&i
print(out)