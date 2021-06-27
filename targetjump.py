t=-7



def recur(t,prev=0,step=1):
    if prev==t:
        return step
    if prev+step>t:
        prev=prev-step
        step=recur(t,prev,step+1)
        return step
    if prev+step<t:
        prev=prev+step
        step=recur(t,prev,step+1)
        return step
    if prev+step==t:
        prev=prev+step
        step=recur(t,prev,step)
        return step
    return step
    
print(recur(t))
