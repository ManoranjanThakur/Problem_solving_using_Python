def recur(n,t):
    if(len(t)>n):
        return t[-1]
    t.append(t[-3]+t[-2]+t[-1])
    recur(n,t)
    return t[-1]

print(recur(25,[0,1,1]))