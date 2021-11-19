class Student:

    def __init__(self, cursor,stu_id='', name = ''):
        self.student_id = stu_id
        self.name = name
        self.cursor = cursor

    def add_student(self):
        #Add student to database here using the cursor passed into the class
        pass

    def remove_student(self):
        #Remove student from DB (Make sure all enrollments are deleted
        pass