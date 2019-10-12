house= [1,2,3,4,5]
n=1
x=[0 for i in range (n)]
index = 0
for h in house:
    print("h: "+str(h))
    print("x["+str(index)+"] = x["+str(index)+"] + "+str(h) +"]" )
    x[index]=x[index]+(h)    
    if index <n-1:     
        
        index+=1
        print("Index"+str(index))
        
        
    else:
        
        index=0
    
print(x)
        
        
        
    
