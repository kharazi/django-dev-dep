class Student:
     
    def __init__(self, firstname, lastname, courses=[], grades=[]): 
        # print("salam man function init hastam") 
        self.courses = courses 
        self.firstname = firstname 
        self.lastname = lastname 
        self.nomreha = grades 
        self.mashroot = False 
        self.avg = self.average() 
         
    def fullname(self): 
        print(self.firstname + self.lastname) 
         
    def average(self): 
        avg = 0 
        sum = 0 
        for n in self.nomreha: 
            sum += n 
        avg = sum / len(self.nomreha) 
        if avg < 14: 
            self.mashroot = True 
        return avg 
         
    def __str__(self): 
        return(self.firstname)

    def __dir__(self): 
        return(["haha"]) 



studentinstances = [
    Student("Vahid", "Kharazi", grades=[1, 2, 4, 20, 5]),
    Student("ALi", "Alavi", grades=[1, 2, 4, 20, 5]),
    Student("ALi", "Alavi", grades=[1, 2, 4, 20, 5])
]

users = [
    {
        "name": "vahid",
        "courses": [1, 2, 4, 20, 5]
    },
    {
        "name": "Ali",
        "courses": [1, 2, 11, 20, 17]
    },
    {
        "name": "Mohammad",
        "courses": [1, 2]
    },
    {
        "name": "Sara",
        "courses": [17, 20, 17]
    },
]

for u in users:
    studentinstances.append(
        Student(u['name'], lastname='', grades=u['courses'])
    )

# print(studentinstances)


def classavg(studentlist):
    sum = 0 
    for student in studentlist:
        sum += student.avg
        print(student.avg, student.firstname)

    return(sum / len(studentlist))


result = classavg(studentinstances)
print(result)

# def average(studentlist):
#     for student in studentlist:
#         sum = 0
#         for g in student['courses']:
#             sum += g
#         avg = sum / len(student['courses'])
#         print("The average of %s is %f." % (
#             student['name'], avg)
#         )
# average(users)