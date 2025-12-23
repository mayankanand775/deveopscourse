#email condition

# a-z  having small cases
#0-9  digits
#. _  time 1 after @
# @ count 1
# from back  . 3 rd and 4th postion
import re
email_condition="^[a-z]+[\._]?[a-z 0-9 ]+[@]\w+[.]\w{3,4}$"
user_email=input("enter your email : ")
if re.search(email_condition,user_email):
    print(" right email")
else:
    print('wrong email')    
