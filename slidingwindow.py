a=[3,6,1,2,3,4,5,6,6,7,3,4,3,3]
n=3
maxsum=-sum(a[0:3])
curr_sum=sum(a[0:3])
i=0
j=n
while(j<len(a)):
    curr_sum=curr_sum-a[i]+a[j]
    if maxsum<curr_sum:
        maxsum=curr_sum
    i+=1
    j+=1
print(maxsum)