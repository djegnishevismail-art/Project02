class Student:
    def __init__(self,grade):
        self.__grade = grade


    def set_grade(self,grade):
        if 0 < grade <= 100:
            self.__grade = grade
        else:
            print("Мындай баа жок")

    def get_grade(self):
        return self.__grade

s1 = Student(0)
s1.set_grade(120)

print(s1.get_grade())
