class un:
    def __init__(self):
        sid=age=marks=0
    def validate_marks(self):
        if(self.marks>=0 and self.marks<=100):
            return True
        else:
            return False
    def validate_age(self):
        if(self.age>20):
            return True
        else:
            return False
    def check(self):
        if(self.validate_marks() and self.validate_age()):
            if(self>=65):
                return True
            else:
                return False
        else:
            return False
    def setter(self,sid,a,m):
        self.sid=sid
        self.age=a
        self.marks=m
    def getter(self):
        if(u.check()):
            print("USER_ID:",self.sid)
            print("AGE:",self.age)
            print("MARKS:",self.marks)
            print("given information is CORRECT")
        else:
            print("INVALID INFORMATION")

            
n=int(input("enter the number of student:"))
for i in range(0,n):
      u=un()
      sid=int(input("enter the id"))
      age=int(input("enter the age"))
      marks=int(input("enter the marks"))
      u.setter(sid,age,marks)
      u.getter()
      
