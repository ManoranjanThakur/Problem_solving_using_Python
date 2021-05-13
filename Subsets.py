def subsets(arr):
    output=[[]]
    for i in arr:
        output+=[j+[i] for j in output]
    return output

print(subsets([1,2,3]))