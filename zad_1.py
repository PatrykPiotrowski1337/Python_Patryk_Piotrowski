class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return """{} Imie studenta \n{} Oceny studenta
        """.format(self.name,self.marks)


    def is_passed(self) -> bool:
        if self.marks>50:
            return True
        return False


student_1 = student("Adam",60)
student_2 = student("Małysz",30)

print(student_2.is_passed())
print(student_1.is_passed())
print(student_1)