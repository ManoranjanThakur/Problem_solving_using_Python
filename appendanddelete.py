def appendAndDelete(s, t, k):
    a=len(s)
    b=len(t)
    var=0
    if a > b:
        var=a-b
        s=s[0:b]
    a=len(s)
    c=a
    for i in range(a):
        if s[i]!=t[i]:
            flag=1
            c=i
            break
        flag=0
    if flag==1:
        s=s[0:c]
        var+=(a-1)-c
        if var>=k and s!=t:
            return ("No")
    for i in range(b):
        if s==t:
            if(var>k):
                return ("No")
            return ("Yes")
        if len(s)<=i:
            s=s+t[i]
            var+=1
        else:
            if s[i]!=t[i]:
                s[i]=t[i]
                var+=1
    if (var>k):
        return ("No")
    elif (var<=k) and s==t:
        return ("Yes")

print(appendAndDelete("ashley","ash",2))