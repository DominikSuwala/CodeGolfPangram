t=0
z=2**26-1
for x in raw_input():
    t|=1<<(31&(ord(x)-65))
print t&z==z
