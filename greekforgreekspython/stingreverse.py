s='i like this program very much'
y=s[::-1]
split=y.split(" ")
k=[]
for i in range(0,len(split)):
    k.append(split[i][::-1])
m=""
for i in range(0,len(k)):
     m=m+k[i]
     m=m+' '


