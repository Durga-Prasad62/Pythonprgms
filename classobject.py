# Question 1:  Create your own class which can implement all arthematic operations. Create 2 objects for it and call above implemented methods. Add model_num, made_in variables to obj1. Add color and discount to obj2. print model_num, made_in, color, discount to both the object

# Question 2:Define self


class Calculator:
    def Add(self,a,b):
        print (a+b)
    def Sub(Self,a,b):
        print(a-b)
    def Mul(self,a,b):
        print(a*b)
    def Div(self,a,b):
        print("division not possible")if b==0 else (b/a)
    def expo(self,a,b):
        print(a**b)
    def floor(self,a,b):
        print(a//b)
    def mod(self,a,b):
        print(a%b)
    def display(self):
        print(self.model_no,self.made_in,self.color,self.discount)
    def display2(self):
        print(self.model_no,self.made_in,self.color,self.discount)
cal1=Calculator()
cal2=Calculator()

cal1.Add(2,4)
cal1.Sub(2,4)
cal1.Mul(2,4)
cal1.Div(2,0)
cal1.mod(2,4)
cal1.expo(2,4)
cal1.floor(2,4)
cal1.model_no=121
cal1.made_in="india"
cal1.color="orange"
cal1.discount=20
cal2.model_no=342
cal2.made_in="russia"
cal2.color="blue"
cal2.discount=10
cal1.display()
cal2.display2()
#define self
# In Python, self is a conventional name for the first parameter of instance methods within a class. 
# It is not a reserved keyword, but its use is a widely adopted convention that significantly improves code readability and maintainability.
# It allows methods to access and manipulate the attributes (variables) and other methods belonging to the specific instance of the class.




