def Repetitions(arr):
    count=1
    maximum=1
    for i in range(len(arr)):
        if (i<len(arr)-1):
            if(arr[i]==arr[i+1]):
                count+=1
                if count>maximum:
                    maximum=count
            else:
                count=1
    return maximum


print(Repetitions(input()))
