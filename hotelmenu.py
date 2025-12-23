#define the menu of restaurant
menu={ 
   'Pizza':40,
   'Pasta':50,
   'Burger':60,
   'salad':70,
   'coffee':80

}
#Greet
print("Welcome to Python restruant !")
print ("Pizza :Rs40\nPasta: Rs50\nBurger: Rs60\nsalad: Rs70\ncoffee: Rs80")

order_total=0

item_1=input("enter the name of the item you want to order = ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your itme {item_1} has been added  to your order")
else:
    print(f"ordered {item_1} is not in the menu")   

another_order= input("do you want to add another item? (Yes/No)")
if another_order=="Yes":
    item_2=input("Enter the name of the second itme = ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"Total amount to be paid {order_total}") 
    else:
        print(f'ordered {item_2} is not in the menu')
elif another_order=="No":
    print(f"Total amount to be paid {order_total}")
    print("thank you for the order")
else:
    print("ops you typed it wrong")
    print(f"Total amount to be paid {order_total}")    
