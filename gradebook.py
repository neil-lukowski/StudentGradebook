##
# Gradebook
#
# Authors: James Nelson & Neil Lukowski
# Project: CS150 Project 4
# Created: 4/18/2019
# Revised 5/3/2019
# This file contains the Gradebook class definition. This class represents an
# entire gradebook of students.
##

import student

class Gradebook:
    """Gradebook class that simulates a gradebook filled with students.
    """
    def __init__(self):
        """Method tat initialies the gradebook list.
        
        Args:
            N/A
        Returns:
            N/A
        """    
        self.gradebook = []
        
    def add_student(self, student):
        """Method that adds a new Student object to the gradebook.
        
        Args:
            student - Represents the student object created in the Student 
            class.
        Returns:
            N/A
        """
        self.gradebook.append(student)
        
    def get_size(self):
        """Method that returns the size of the gradebook.
        
        Args:
            N/A
        Returns:
            Returns an int value corresponding to the size of the gradebook.
        """
        return len(self.gradebook)
        
    def get_student(self, student_id):
        """Method that retrieves a student's information by their ID in the
        gradebook.
        
        Args:
            student_id - This represents the students position in the gradebook
            list.
        Returns:
            Returns the id of the student
        """
        return self.gradebook[student_id]
        
    def apply_curve(self, category, curve):
        """Method that accepts a string for category and value for curve, then
        applies the curve to that category
        
        Args:
            category - a string representing the grade category
            curve - an integer by which to curve the grade category
        Returns:
            N/A
        """
        
        if category.upper() == 'HW':
            for student in self.gradebook:
                student.curve_homework(curve)
        elif category.upper() == 'PROJECT':
            for student in self.gradebook:
                student.curve_project(curve)
        elif category.upper() == 'TEST':
            for student in self.gradebook:
                student.curve_test(curve)
            
    def calc_ov_avg(self):
        """Method that calculates the overall average grade of the student
        
        Args:
            N/A
        Returns:
            N/A
        """
        for student in self.gradebook:
            student.set_overall()
            
    def print_stats(self):
        """Method that formats and prints a string composed of the overall 
        grades for homework, tests, projects across all students
        
        Args:
            N/A
        Returns:
            N/A
        """
        tot_hw = 0
        tot_proj = 0
        tot_test = 0
        
        for student in self.gradebook:
            tot_hw = student.get_hw_avg() + tot_hw
        tot_hw = tot_hw / self.get_size()
        for student in self.gradebook:
            tot_proj = student.get_proj_avg() + tot_proj
        tot_proj = tot_proj / self.get_size()
        for student in self.gradebook:
            tot_test = student.get_test_avg() + tot_test
        tot_test = tot_test / self.get_size()
        
        print("HW AVG: " + str(int(tot_hw)) + "; TEST AVG: " + str(int(tot_test)) + \
            "; PROJ AVG: " + str(int(tot_proj)))
        
    def find_top_student(self):
        """method that takes no arguments and returns an integer representing 
        the ID (position of the student in the gradebook) of the student with 
        the highest overall average. This method uses a while loop to find 
        the student with the top average
        
        Args:
            N/A
        Returns: integer representing the index position of the student with the
        highest grade average
        """
        
        max = 0 
        i=0
        while i < len(self.gradebook):
            if max < self.gradebook[i].get_tot_avg():
                max = self.gradebook[i].get_tot_avg()
            i += 1
        return i
        
    def print_single_student(self, student_id):
        """This method accepts the ID as an argument and calls that student's
        print_student() method
        
        Args:
            ID of the student represented as index value
        Returns:
            N/A
        """

        self.gradebook[student_id].print_student()
        
    def print_all_students(self):
        """This method uses a while loop and each student's print_student() 
        method to print the information of all students in formatted fashion
        
        Args:
            N/A
        Returns:
            N/A
        """
        i=0

        while i < len(self.gradebook):
            index = i
            print("ID: " + str(index) , end = ' ')
            self.gradebook[index].print_student()
            i += 1
   
     
def test_gradebook():
    
    gb1 = Gradebook()
    gb1.add_student(student.Student(70, 80, 90))
    gb1.add_student(student.Student(75, 85, 95))
    gb1.add_student(student.Student(2, 10, 0))
    gb1.add_student(student.Student(170, 30, -90))
    
    gb1.calc_ov_avg()
    gb1.print_stats()
    #print(gb1.get_student(0))
    gb1.apply_curve('hw', 6)

    gb1.calc_ov_avg()
    #gb1.print_stats()
    print(gb1.find_top_student())
    #gb1.print_single_student(0)
    #gb1.print_all_students()
    

    print(s1.get_hw_avg())
    print(s1.get_proj_avg())
    print(s1.get_test_avg())
    print(s1.get_tot_avg())
    
    s1.curve_test(10)
    s1.curve_project(10)
    s1.curve_homework(10)
    
    s1.set_overall()
    
    print(s1.get_hw_avg())
    print(s1.get_proj_avg())
    print(s1.get_test_avg())
    print(s1.get_tot_avg())
    
    s1.gen_grade_message()
    
    s1.print_student()
    

if __name__ == '__main__':
    test_gradebook()