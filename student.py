##
# Student
# 
# Authors: James Nelson & Neil Lukowski
# Project: CS150 Project 4
# Created: 4/18/2019
# Revised: 5/3/2019
# This file contains the Student class definition. This class represents an
# individual student.
##

class Student:
    """Student class for representing a student individual. Allows for curving
    grades.
    """
    
    def __init__(self, hw_avg, proj_avg, test_avg, tot_avg = 0):
        """Initializes the fields for the Student class and the named constants
        representing the different weights of each area.
        
        Args:
            hw_avg - Represents the student's individual homework average.
            proj_avg - Represents the student's individual project average.
            test_agv - Represents the student's individual test average.
            tot_avg - Represents the student's overall average. Starts at zero.
        Returns:
            N/A
        """
        
        self.HW_WEIGHT = .2
        self.PROJ_WEIGHT = .4
        self.TEST_WEIGHT = .4
        
        self.hw_avg = hw_avg
        self.proj_avg = proj_avg
        self.test_avg = test_avg
        self.tot_avg = tot_avg
        
    def get_hw_avg(self):
        """Getter method used to return homework average.
        
        Args:
            N/A
        Returns:
            Returns an int value for homework average.
        """
        
        return self.hw_avg
        
    def get_proj_avg(self):
        """Getter method used to return project average.
        
        Args:
            N/A
        Returns:
            Returns an int value for project average.
        """
        
        return self.proj_avg
        
    def get_test_avg(self):
        """Getter method used to return test average.
        
        Args:
            N/A
        Returns:
            Returns an int value for test average.
        """
        
        return self.test_avg
        
    def get_tot_avg(self):
        """Getter method used to return total average.
        
        Args:
            N/A
        Returns:
            Returns an int value for total average.
        """    
        return self.tot_avg
        
    def curve_test(self, curve):
        """Method that curves the test value.
        
        Args:
            curve - Value representing the points added to the test average.
        Returns:
            N/A
        """
        curve_amt = curve
        self.test_avg = self.test_avg + curve_amt
        
    def curve_project(self, curve):
        """Method that curves the project value.
        
        Args:
            curve - Value representing the points added to the project average.
        Returns:
            N/A
        """
        curve_amt = curve
        self.proj_avg = self.proj_avg + curve_amt
        
    def curve_homework(self, curve):
        """Method that curves the homework value.
        
        Args:
            curve - Value representing the points added to the homework average.
        Returns:
            N/A
        """
        curve_amt = curve
        self.hw_avg = self.hw_avg + curve_amt
        
    def set_overall(self):
        """Method that calculates the overall average using the individual
        values and incorperating the different weights.
        
        Args:
            N/A
        Returns:
            N/A
        """
        self.tot_avg = int(self.hw_avg * self.HW_WEIGHT + self.proj_avg * self.PROJ_WEIGHT \
            + self.test_avg * self.TEST_WEIGHT)
            
    
    def gen_grade_message(self):
        """Method that generates a grade message based on the student's overall
        average.
        
        Args:
            N/A
        Returns:
            Returns a string corresponding to the student's overall grade.
        """
        response_str = ''
        
        A = 90.0
        B = 80.0
        C = 70.0
        D = 60.0
        
        if self.tot_avg >= A:
            response_str = 'GREAT!'
        elif self.tot_avg >= B:
            response_str = 'GOOD!'
        elif self.tot_avg >= C:
            response_str = 'OKAY!'
        elif self.tot_avg >= D:
            response_str = 'STUDY MORE!'
        else:
            response_str = 'DANGER!'
            
        return response_str
    
    def print_student(self):
        """Method that prints the individual student's averages and the string
        corresponding to their overall average.
        
        Args:
            N/A
        Returns:
            N/A
            
        """
        
        print("(HW: " + str(self.hw_avg) + "; TESTS: " + str(self.test_avg) + ";"\
            + ' PROJECTS: ' + str(self.proj_avg) + '; OVERALL: '\
            + str(self.tot_avg) + '; STATUS: ' + str(self.gen_grade_message()) + ')')


            
def test_student():
    s1 = Student(70, 80, 90)
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
    test_student()
