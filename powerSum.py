def powerSum(X,N,n=1):
    result=n**N
    if result>X:
        return 0
    if result==X:
        return 1
    if result<X:
        return powerSum(X,N,n+1)+powerSum(X-result,N,n+1)
    
print(powerSum(100,2))