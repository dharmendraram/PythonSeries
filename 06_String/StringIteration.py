#to use range
w="Welcome to Ram"
# w=w[-1::-1]  #reverse
# t=len(w)
# print(t) #14
# for a in range(t):
#     print(w[a])   
#w[0]=w
#w[1]=e

# print("Reverse")

# for a in range(t-1,-1,-1):
#     print(w[a])

#Another method

for a in w:
    print(a)

#if we reverse then firstly reverse then print
w=w[-1::-1]
for b in w:
    print(b)
