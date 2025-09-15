from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def Role(self):
        pass
@abstractmethod
class Student(Person):
    def __init__(self,student_id,name,age):
        super().__init__(name,age)
        self.student_id=student_id
        self.enrolled_courses=[]
    def Role(self):
        return'student'
    def get_enrolled_courses(self):
        print(self.enrolled_courses)
   
    def add_enrolled_courses(self,coursename):
        if coursename not in  self.enrolled_courses :
          return self.enrolled_courses.append(coursename)
        else:
            pass
class Teacher(Person):
   def __init__(self, teacher_id):
       self.teacheher_id=teacher_id
       self.enrolled_courses=[]
   def  assaigned_course_list(self):
       print(self.enrolled_courses)
   def get_assaigned_course_list(self,asign_course_list):
         if  self.enrolled_courses not in  asign_course_list :
          return self.enrolled_courses.append(asign_course_list)
         else:
            pass
class Course:
    pass
      
       
        
stu1=Student(1,'mahesh',20)
stu2=Student(2,'ramu',21)
stu1.add_enrolled_courses('DBMS')
stu1.add_enrolled_courses("DBMS")
stu1.add_enrolled_courses("PYTHON")
stu1.add_enrolled_courses("JAVA")

stu2.add_enrolled_courses('DBMS')
stu2.add_enrolled_courses("DBMS")
stu2.add_enrolled_courses("PYTHON")
stu2.add_enrolled_courses("PYTHON")
stu2.add_enrolled_courses("OOPS")
print(stu1.enrolled_courses)
print(stu2.enrolled_courses)
# t1=Te.acher()




