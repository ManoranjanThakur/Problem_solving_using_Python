n=5
k=3
sum=0
for i in range(1,n+1):
    sum+=(2*i-1)**k
print(sum)
# 1**3 + 2**3 + 3**3 + 4**3 + 5**3

# def recur(n,k,a=n):
#     if a==1:
#         return 1
#     sum=recur(n,k,a-1)
#     return sum+a**k
# print(recur(n,k))