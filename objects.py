from typing import List, Dict


class Student:

    def __init__(self, cursor, stu_id='', name=''):
        self.student_id = stu_id
        self.name = name
        self.cursor = cursor

    def add_student(self):
        # Add student to database here using the cursor passed into the class
        pass

    def remove_student(self):
        # Remove student from DB (Make sure all enrollments are deleted
        pass


class Course:

    def __init__(self, cursor, c_id='', c_desc='', creds=0):
        self.cursor = cursor
        self.course_id = c_id
        self.course_description = c_desc
        self.credits = creds

    def add_course(self):
        # Add course to DB using cursor passed into class
        pass

    def remove_course(self):
        # you get the idea
        pass


class Enrollment:

    def __init__(self, cursor):
        self.cursor = cursor
        self.student_id = ''
        self.course_id = ''
        self.flag = 0

    #  This checks to see if the credits has exceeded the 12 threshold
    #  I have each class being 4 credits and therefore if it is over 3 classes, the last one
    #  will have the flag
    #  This should also be done with an SQL query like on the board, but to set the flag is going
    #  to be nearly identical.
    def check_credits(self, course_list: Dict, enroll_list: List):
        total_credits = 0
        if len(enroll_list) > 0:
            for enroll in enroll_list:
                total_credits += course_list[enroll.course_id].credits

        if total_credits + course_list[self.course_id].credits > 12:
            return True
        else:
            return False

    #  This will be replaced with SQL queries, but for now my return is acting like the INSERT
    def add_enrollment(self, stu_id, c_id, course_list: Dict, enroll_list: List):
        course = course_list[c_id]
        self.student_id = stu_id
        self.course_id = c_id

        if self.check_credits(course_list, enroll_list):
            self.flag = 1
        else:
            self.flag = 0

        # self.to_string()
        return self

    def to_string(self):
        print("Student ID:", self.student_id, "\tCourse ID:", self.course_id, "\tFlag:", self.flag)
