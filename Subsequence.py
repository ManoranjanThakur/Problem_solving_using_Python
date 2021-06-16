b= 'abc'
a= 'aaa'

def subseq(word):
    if len(word)==0:
        return [""]
    small=subseq(word[1:len(word)])
    result=[""]*(2*len(small))
    k=0
    for i in range(len(small)):
        result[k]=small[i]
        k=k+1
    for i in range(len(small)):
        result[k]=word[0]+small[i]
        k=k+1
    return result

print(subseq(b))
