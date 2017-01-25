t=0
z=2**26-1
for x in raw_input():
    t|=1<<abs(((ord(x))&-33)-65)
print 1 if t&z==z else 0
