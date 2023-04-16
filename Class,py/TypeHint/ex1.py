from typing import List, Tuple, Dict

Numbers = List[int]

def findNumber(numbers:Numbers, searchNum:int) -> int:
    return numbers.index(searchNum)

StudentId = int
StudentName = str
StudentScore = int
# Student = Tuple[StudentId, StudentName]
Student = Tuple[StudentScore, StudentName]
AvgScore = float

# def printStudentInfo(student:Student) -> None:
#     print(f"ID:{student[0]} Name:{student[1]}")

# printStudentInfo((10, "Smith"))

Students = Dict[StudentId, Student]
def getScoreAvg(students:Students) -> float:
    s = 0
    for score, _ in students.values():
        s += score
    return s / len(students)

students = {
    1:(100, "Tom"),
    2:(50, "Smith"),
    3:(10, "Davin")
}

print(getScoreAvg(students))