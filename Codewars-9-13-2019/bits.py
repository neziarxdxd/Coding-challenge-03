import numpy

x=[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
size= len(x) // 8
x=([(x[(0+(i*8)):(8+(i*8))]) for i in range(size)])[::-1]
t= []
for i in x:
    t+=i
print(t)


