#single inheritance one child class nd one parent class
class parent():
    def f1(self):
        print("its a parent class")
class child(parent):
    def f2(self):
        print("its a child class")
obj=child()
obj.f2()
obj.f1()
    
            