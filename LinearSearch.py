def LS(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            print(i)
            return
    print('Not present')
LS([1,2,3,4],7)



