# need a student based clg management system: 


class Student:
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score
        self.department = None



class Staff:
    def __init__(self, staff_id, name, designation):
        self.staff_id = staff_id
        self.name = name
        self.designation = designation
        self.department = None

    def assign_department(self, department):
        self.department = department


class Department:
    def __init__(self, name, seats):
        self.name = name
        self.available_seats = seats
        self.students = []
        self.staffs = []

    def allocate_student(self, student):
        if self.available_seats > 0:
            self.available_seats -= 1
            self.students.append(student)
            student.department = self.name
            return True
        return False

    def add_staff(self, staff):
        self.staffs.append(staff)
        staff.department = self.name




cs = Department("CS", 2)


staff1 = Staff(1, "Dr. Kumar", "Professor")
staff2 = Staff(2, "Priya", "Assistant Professor")

cs.add_staff(staff1)
cs.add_staff(staff2)

print(cs.staffs[0].name)
print(cs.staffs[1].designation)
staff_data = []
for i in cs.staffs:
    dic = {}
    dic["name"] = i.name
    dic["designation"] = i.designation
    staff_data.append(dic)

print(staff_data)






# class Student:
#     count = 0
#     def __init__(self, stud_name, stud_roll):
#         self.stud_name = stud_name
#         self.stud_roll = stud_roll
#         self.stud_dept = self.get_dept

#         Student.count +=1 


#     @classmethod
#     def csa(cs,self):
#         no_of_seats = 100
#         score_optained = 90
#         if cs.count <= no_of_seats: 
#             return("Seats are avail")
#         else:
#             return("No Seat")


#     def mech(self):
#         no_of_seats = 105


#     def eee(self):
#         no_of_seats = 500



#     def get_dept(self, dept):
#         return dept