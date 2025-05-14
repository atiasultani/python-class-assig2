# in class Assigment 9/may/2025
# University Manegement System created by class or OOP Mathods

# entities 
# 1-Students
# 2-Course
# 3-Instractor
# 4-Department

class Persons:  #blue print
    def __init__(self,name,age): # parameterized constractor 
        self.name=name  #attributies or variable
        self.age=age
    
    def getname(self): #method or function
            return(f"Name is :{self.name}")
      
        
class Student(Persons):
        def __init__(self,name,age,rollNo,course):
            super().__init__(name,age) #inharitance
            self.rollNo=rollNo
            self.course=course
        def display(self):
            print(f"Studend name is : {self.name} \n RollNo is :{self.rollNo} \n course : {self.course}" )

s1=Student("hamza",25,1,["asd","zxc","lmn"])
s1.display()    

class Instractor(Persons):
        def __init__(self,name,age,salary,assign_course):
            super().__init__(name,age) #inharitance
            self.salary=salary
            self.assign_course=assign_course
        def display(self):    #polymorphsim
            print(f"Instractor name is : {self.name} \n  age is :{self.age} \n salary is : {self.salary} \n " )
        
ins1=Instractor("sir zia",55,500000,["a.i","web3.0","piaic"])
ins1.display()

