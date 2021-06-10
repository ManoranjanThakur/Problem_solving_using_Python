import math
Stuart=0
Kevin=0
S="BANANA"
for i in range(len(S)):
    if (S[i].lower()=='a') or (S[i].lower()=='e') or (S[i].lower()=='i') or (S[i].lower()=='o') or (S[i].lower()=='u'):
        Kevin+=math.factorial(len(S[i:]))
    else:
        Stuart+=math.factorial(len(S[i:]))
print(Stuart,Kevin)
