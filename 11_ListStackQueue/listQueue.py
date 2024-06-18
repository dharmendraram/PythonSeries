#Queue-> linear data structure(FIFO)
#Enqueue-adds an item to the queue
#Dequeue-removes item from thr queue
#Front-get the last item from queue
l=[]
while True:
    c=int(input('''
        1 Enqueue
        2 Dequeue
        3 Front
        4 Rear
        5 Exit
        '''))
    if c==1:
        n=input("Enter the value")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Queue")
        else:
            del l[0]
            print(l)
    elif c==3:
        if len(l)==0:
            print("Empty Queue")
        else:
            print("First Queue value:-", l[0])
    elif c==4:
        if len(l)==0:
            print("Empty Queue")
        else:
            print("Last Queue value:- ", l[-1])
    elif c==5:
        break
    else:
        print("Invalid Opr..")

