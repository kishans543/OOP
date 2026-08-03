class Student:
    def __init__(self,name,roll,marks):
        self.name = name 
        self.roll = roll
        self.marks = marks
    def display(self):
        print("name : " , self.name)    
        print("roll : " , self.roll)
        print("marks : " , self.marks)  
    def average(self):
        return sum(self.marks)/ len(self.marks)
    

s1 = Student("kishan" , 751 , [87,45,85])
s1.display()
print("average :" ,s1.average())


        