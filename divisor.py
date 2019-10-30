def divisor(num):
    for i in range(1,num):
        if num%i==0:
            print(i)
            
num=int(raw_input("enter the number"))
print("Divisor of ",str(num),"are:")
divisor(num)
