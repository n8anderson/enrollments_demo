from objects import *

def main():
    new_student = Student("Cursor", "004221", "Nate Anderson")

    course1 = Course("Cursor", '101', 'Web App', 4)
    course2 = Course("Cursor", '102', 'Web', 4)
    course3 = Course("Cursor", '103', 'App', 4)
    course4 = Course("Cursor", '104', 'WEPA', 4)

    #pseudo courses table
    course_dict = {'101': course1,
                   '102': course2,
                   '103': course3,
                   '104': course4}

    #pseudo enrollments table
    enrollments = []

    #Creating new enrollment objects to use Ignore cursor
    new_enrollment = Enrollment("Cursor")
    new_enrollment1 = Enrollment("Cursor")
    new_enrollment2 = Enrollment("Cursor")
    new_enrollment3 = Enrollment("Cursor")

    #Adding the enrollments to the DB (This will be done in your method in the class through SQL)
    #For simplicities sake I am pretending my db is this dictionary and adding it to that instead
    enrollments.append(new_enrollment.add_enrollment(new_student.student_id, course1.course_id,
                                                     course_dict, enrollments))

    enrollments.append(new_enrollment1.add_enrollment(new_student.student_id, course2.course_id,
                                                      course_dict, enrollments))

    enrollments.append(new_enrollment2.add_enrollment(new_student.student_id, course3.course_id,
                                                      course_dict, enrollments))

    enrollments.append(new_enrollment3.add_enrollment(new_student.student_id, course4.course_id,
                                                      course_dict, enrollments))

    #  Outputting the enrollments "table" to show that a flag was added to the last course when
    #  the 12 credits threshold has been broken
    for i in enrollments:
        i.to_string()


main()