
from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum


class Department(Enum):
    CS = ("CS", 90)
    MECH = ("MECH", 88)
    EEE = ("EEE", 88)
    CIVIL = ("CIVIL", 82)

    def __init__(self, code, score):
        self.code = code
        self.score = score
        
    @classmethod
    def find_dept_same_score(cls):
        dic = {}
        for dept in Department:
            score = dept.score
            if score not in dic:
                dic[score] = []

            dic[score].append(dept)

        return dic



@dataclass
class Student(ABC):

    stud_name: str
    stud_age: int
    stud_marks: int
    department: Department

    def find_same_score_department(self):

        dic_scores = Department.find_dept_same_score()
        same_depts = dic_scores[self.department.score]

        same_depts = [
            dept
            for dept in same_depts
            if dept != self.department
        ]

        # return [
        #     dept
        #     for dept in dic_scores[self.department.score]
        #     if dept != self.department
        # ]
        return same_depts

    def get_same_department_fee(self):

        same_depts = self.find_same_score_department()

        if same_depts:

            print(
                f"{self.department.code} has same score with: "
                f"{[dept.code for dept in same_depts]}"
            )

            fees = {
                self.department.code: self.course_fees()
            }

            for dept in same_depts:
                dept_class = DEPARTMENT_CLASSES[dept]
                other_stud = dept_class(
                    self.stud_name,
                    self.stud_age,
                    self.stud_marks,
                    dept
                )

                fees[dept.code] = other_stud.course_fees()

            return fees
        return None



    @abstractmethod
    def course_fees(self):
        pass

    @abstractmethod
    def dept_eligible(self):
        pass


@dataclass
class CivilDepartment(Student):

    def course_fees(self):
        return 1000

    def dept_eligible(self):

        same_fee = self.get_same_department_fee()

        if same_fee is not None:
            return same_fee

        if self.stud_marks > self.department.score:
            return self.course_fees()

        return "Not eligible for Civil"


@dataclass
class CSDepartment(Student):

    def course_fees(self):
        return 1000

    def dept_eligible(self):

        same_fee = self.get_same_department_fee()

        if same_fee is not None:
            return same_fee

        if self.stud_marks > self.department.score:
            return self.course_fees()

        return "Not eligible for CS"


@dataclass
class MechDepartment(Student):

    def course_fees(self):
        return 1200

    def dept_eligible(self):

        same_fee = self.get_same_department_fee()

        if same_fee is not None:
            return same_fee

        if self.stud_marks > self.department.score:
            return self.course_fees()

        return "Not eligible for Mech"


@dataclass
class EEEDepartment(Student):

    def course_fees(self):
        return 1500

    def dept_eligible(self):

        same_fee = self.get_same_department_fee()

        if same_fee is not None:
            return same_fee

        if self.stud_marks > self.department.score:
            return self.course_fees()

        return "Not eligible for EEE"


DEPARTMENT_CLASSES = {
    Department.CS: CSDepartment,
    Department.MECH: MechDepartment,
    Department.EEE: EEEDepartment,
    Department.CIVIL: CivilDepartment
}


stud_1 = MechDepartment("DK",20,90,Department.MECH)
print(stud_1.dept_eligible())

# @dataclass   
# class Student(ABC):
#     stud_name : str
#     stud_age : int
#     stud_roll : int
#     stud_marks : int
#     department : Department

#     @abstractmethod
#     def course_fees(self):
#         pass

#     @abstractmethod
#     def dept_eligible(self):
#         pass

# @dataclass
# class CivilDepartment(Student):

#     def course_fees(self):
#         return 1000

#     def dept_eligible(self):
#         if self.stud_marks > 70:
#             return self.course_fees()
        
#         return "Not eligible for Civil"

# @dataclass
# class CSDepartment(Student):

#     def course_fees(self):
#         return 1000

#     def dept_eligible(self):
#         if self.stud_marks > 90:
#             return self.course_fees()
        
#         return "Not eligible for CS"

# @dataclass
# class MechDepartment(Student):

#     def course_fees(self):
#         return 1000

#     def dept_eligible(self):
#         if self.stud_marks > 80:
#             return self.course_fees()
        
#         return "Not eligible for mech"


# @dataclass
# class EEEDepartment(Student):

#     def course_fees(self):
#         return 1000

#     def dept_eligible(self):
#         dic_scores = Department.find_dept_same_score()
#         if len(dic_scores.values()) > 1:
            
#             if self.stud_marks > self.department.score:
#                 return self.course_fees()
        
#         return "Not eligible for EEE"




