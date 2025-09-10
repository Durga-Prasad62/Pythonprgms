#Person

from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Person constructor called')

    @abstractmethod
    def print_role(self):
        pass


class Student (Person):

    def __init__(self, student_id, name, age):
        super().__init__(name, age)
        self.student_id = student_id
        self.sd_courses_list = []


    def print_role(self):
        return 'Student'
    

    def enroll_to_course(self, course_name):
        self.sd_courses_list.append(course_name)

    def show_enrolled_courses(self):
        print(self.sd_courses_list)

    
    def __str__(self):
        return str(self.student_id)
    


    

std1 = Student(1, 'Mahesh', 25)
print(std1)

std1.show_enrolled_courses()
std1.enroll_to_course('DBMS')
std1.enroll_to_course('OOPS')
std1.enroll_to_course('OS')
std1.show_enrolled_courses()