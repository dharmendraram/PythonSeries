#stack -> linear data structure
# push-inserting an Element
# pop-deletion an Element
# peek-Display last element
# Display-Display list

l=[]
while True:
    c=int(input('''
        1 Push 
        2 Pop
        3 Peek
        4 Display
        5 Exit
        '''))
    if c==1:
        n=input("Enter the value:")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("List is Empty Stack")
        else:
            p=l.pop()
            print(p)
            print(l)
     
    elif c==3:
        if len(l)==0:
            print("List is Empty Stack")
        else:
           print("Last Stack Value", l[-1])
    elif c==4:
        print("Display Stack",l)
    elif c==5:
        break
    else:
        print("Invalid Opr....")