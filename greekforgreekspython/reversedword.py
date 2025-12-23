s = "["
count=0
if len(s)==1:
     count=count+1

dic={'[':1,']':-1,'(':2,')':-2,'{':3,'}':-3 }
l=s[0:int(len(s)/2)]
k=s[int(len(s)/2):len(s)]

z=0
ma=[]
ya=[]

for i in l:
     ma.append(dic[i])
for j in k:
    ya.append(dic[j]) 
sa=ya[::-1]      

for i in range(0,len(ma)):
     if ma[i]==-(sa[i])and len(s)!=1:
          
          count=0
     else:
          count=count+1  


print(count)             
