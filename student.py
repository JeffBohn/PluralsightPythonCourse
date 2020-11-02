students = []

class Student:

    school_name = "Springfield Elemetary"

    def __init__(self, name, student_id=332):
        self.name = name.strip()
        self.student_id = student_id
        students.append(self)
        self.add_student(name, student_id)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

    def add_student(self, name, student_id=332):
        """
        Adds the student to the student list.
        :param name: string - student name
        :param student_id: integer - optional student ID
        :return: none
        """
        self.name = name.strip()
        self.student_id = student_id
        students.append(self)
