def jumpingOnClouds(c):
    k=0
    i=0
    while(i<len(c)-1):
        if len(c)-1>=i+2 and c[i+2]==0:
            k+=1
            i+=2
        elif len(c)-1>=i+1 and c[i+1]==0:
            k+=1
            i+=1
    return k
c=[0,0,0,0,1,0]
print(jumpingOnClouds(c))