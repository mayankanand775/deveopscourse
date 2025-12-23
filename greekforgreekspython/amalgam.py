s1='allergy'
s2='allergic'
s=list(s1)
x=list(s2)
s.sort()
x.sort()
if ''.join(s)==''.join(x):
    print('true')
else:
    print('False')    