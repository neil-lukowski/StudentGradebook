##
# Driver for GradeBook and Student
#
# Authors: James Nelson & Neil Lukowski
# Project: CS150 Project 4
# Date: 4/18/2019
#
##

import gradebook
import student

def main():
    """
    main driver function that creates the gradebook and populates it with
    5 students and contains all the prompts for user input
    
    Args:
        N/A
    Returns:
        N/A
    """
    
    gb_1 = gradebook.Gradebook()
    
    s1 = student.Student(90, 75, 60)
    gb_1.add_student(s1)
    s2 = student.Student(57, 66, 75)
    gb_1.add_student(s2)
    s3 = student.Student(77, 82, 93)
    gb_1.add_student(s3)
    s4 = student.Student(85, 82, 74)
    gb_1.add_student(s4)
    s5 = student.Student(72, 95, 93)
    gb_1.add_student(s5)
    
    gb_1.calc_ov_avg()
    gb_1.print_all_students()
    gb_1.print_stats()
    top = gb_1.find_top_student() - 1
    print('Highest --> ID:', top, end = ' ')
    gb_1.print_single_student(top)
    
    hw_cve = input("Homework Curve: ")
    tst_cve = input("Test Curve: ")
    prj_cve = input("Project Curve: ")
    
    gb_1.apply_curve(hw_cve, tst_cve, prj_cve)
    
if __name__ == '__main__':
    main()
    
""""    
The driver file should have a main() function that should in order do the following in order. It is fine to use
helper functions that the main() function calls do parts of the following.
1) Add students to an instance of a GradeBook class with the following values:
Student 0 → HW: 90; TESTS: 75; PROJ: 60
Student 1 → HW: 57; TESTS: 66; PROJ: 75
Student 2 → HW: 77; TESTS: 82; PROJ: 93
Student 3 → HW: 85; TESTS: 82; PROJ: 74
Student 4 → HW: 72; TESTS: 95; PROJ: 93
2) Output in order
a) information for each students
b) the HW average, project average, and Test average over all students.
c) information for the student with the highest overall average.
3) Curve the grades after prompting for the homework, test, and project curves to be applied to each student.
This part involves getting user input for the size of the curve.
4) Output in order
a) the homework average, project average, and test average over all students.
c) information for the student with the highest overall average.
4) Repeatedly prompts the user for a student ID and
If a user enters a number that is outside of the gradebook, the loop should not print anything
If a user enters -1 the loop (and the program) should terminate.
Prints the specific student information if a valid student id is entered
"""