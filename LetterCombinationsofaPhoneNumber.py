digit=str(input())
phndic={2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv" ,9:"wxyz"}
if len(digit)==0:
    print([""])
output=[""]
for i in digit:
    tmp=[]
    for j in phndic[int(i)]:
        for o in output:
            tmp.append(o+j)
    output=tmp
print(output)