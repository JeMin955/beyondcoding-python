class Person:
    def __init__(self, name, age, address, nationality):
        self.name = name
        self.age = age
        self.address = address
        self.nationality = nationality

    def introduce(self):
        print("저는 {self.name}이고, 나이는 {self.age}살이고, 주소는 {self.address}이고, 국적은 {self.nationality}이다.")
    
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

class Student(Person):
    def __init__(self, name, age, address, nationality, school, grade):
        Person.__init__(self, name, age, address, nationality)
        self.school = school
        self.grade = grade

p = Person("사람1", 20, "asdf", "한국")
p.name = "사람사람"
p.introduce()

minsu = Student("민수", 15, "asdf", "한국", "OO중학교", 1)
minsu.introduce()