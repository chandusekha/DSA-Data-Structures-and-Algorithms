def generateSubsets(s,l,curr='',i=0):
    if i==len(s):
        l.append(curr)
        return
    generateSubsets(s,l,curr,i+1)
    generateSubsets(s,l,curr+s[i],i+1)
def powerSet(s):
    #code here
    l=[]
    generateSubsets(s,l)
    return l

print(powerSet('abc'))