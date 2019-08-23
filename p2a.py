def search(lis,a):
        print(lis)
        if a in lis:
            return True
        else:
            return False
lis=[]
n=int(raw_input("enter the value:"))
while len(lis)!=n:

    a=int(raw_input("enter the numbers:"))
    if a!=-1:
        lis.append(a)
    else:
            break
b=raw_input("enter the elements to be searched:")
print(search(lis,int(b)))
