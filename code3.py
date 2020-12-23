word=list(input())
mx=1
count=1
for i in range(0,len(word)-1):
    if word[i]==word[i+1]:
        count= count + 1
        if mx>=count:
            pass
        else:
            mx=count
    if word[i]!=word[i+1]:
        count=1
print(mx)
        
    


