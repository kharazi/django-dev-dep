class MashrootException(Exception):
    pass


class Human:

    def __init__(self, first_name, last_name):
        print("Hello I'm a human")
        self.first_name = first_name
        self.last_name = last_name
    
    def get_fullname(self):
        return self.first_name + ' ' + self.last_name

    def say_hello(self):
        print("Salam, man Human hastam") 

    def __str__(self):
        return self.get_fullname()
    
class Student(Human):

    def __init__(self, fname, lname, grades=[]):
        # print("Hello I'm a Student")
        # self.first_name = first_name
        # self.last_name = last_name
        super().__init__(fname, lname)
        self.grades = grades

    def set_father_name(self, father_name):
        self.father_name = father_name

    def get_average(self):
        s = 0
        for g in self.grades:
            s += g
        # if len(self.grades) == 0:
        #     return 0
        # else:
        # try:
        if s / len(self.grades) < 12:
            raise MashrootException
        return s / len(self.grades)
        # except ZeroDivisionError:
        #     return 0
        # except KeyError:
        #     print('key error khordam')
        #     return 1

    def say_hello(self):
        print("Salam, man Student hastam") 


class Teacher(Human):

    def say_hello(self):
        print("Salam, man Teacher hastam")

    def set_grade(self, student_object, gg):
        # print("student object is", student_object, gg)
        # print("grade is:", student_object.grades)
        student_object.grades.append(gg)

    def set_grades(self, student_object, grade):
        student_object.grades += grade

    def set_any_grade(self, student_object, grade):
        if type(grade) == list:
            self.set_grades(student_object, grade)
        elif type(grade) == int:
            self.set_grade(student_object, grade)
        else:
            print("Eshtebah mizani")
        # print(type(grade))



class Course:

    def __init__(self, name, teacher, students):
        self.name = name
        self.teacher = teacher
        self.students = students
        # print('$$$$', self.students)


    def get_class_average(self):
        sum = 0
        for s in self.students:
            try:
                sum += s.get_average()
            except MashrootException:
                sum += 0
        return sum / len(self.students)

    def add_student(self, stu):
        self.students.append(stu)


ali = Human('Ali', 'Alavi')
vahid = Student('vahid', 'kharazi', grades=[1, 2, 3])
sara = Student('Sara', 'Saravi', grades=[3, 10, 20, 18])
majid = Student('Majid', 'Majd', grades=[3, 11, 3])
ahmad = Teacher('Ahmad', 'Ahmadi')

# print(ahmad.get_fullname())
# print(vahid.get_fullname())

django = Course(name="Django2019", teacher=ahmad, students=[vahid, sara])
avg = django.get_class_average()
print(django.name, avg)
# print(django.teacher)

react = Course(name="React2019", teacher=ahmad, students=[majid])
print(react.name, react.get_class_average())

# print(len(django.students))
# django.add_student(majid)
# print(django.get_class_average())
# print(len(django.students))

# print(vahid.say_hello())

# ahmad.set_any_grade(vahid, 10)
# ahmad.set_any_grade(vahid, [12, 16])
# ahmad.set_any_grade(vahid, "salam")
# print(vahid.grades)
# print(vahid.get_average())
# print(ali )
# sara = Student('Sara', 'Saravi', grades=[3, 10, 20, 18])
# mohammad = Student('Mohammad', 'Mahdavi')





# print(ali.get_fullname())
# print(ali.say_hello())
# print(vahid.get_fullname(), vahid.get_average())
# print(sara.get_fullname(), sara.get_average())
# print(mohammad.get_fullname(), mohammad.get_average())



# print(vahid.grades)
# ahmad = Teacher('Ahmad', 'Ahmadi')
# ahmad.say_hello()

# ahmad.set_grade(vahid, 16)
# ahmad.set_grade(vahid, 20)
# ahmad.set_grade(vahid, 0)


# for g in [16, 20, 0, 10, 11, 16]:
#     ahmad.set_grade(vahid, g)
# 

# ahmad.set_grades(vahid, [16, 20, 0, 10, 11, 16])
# print(vahid.grades)
# ahmad.set_grade("salam", 20)
# fullname = mohammad.get_fullname
# print(type(fullname))
# print(type(mohammad))
# print(fullname())