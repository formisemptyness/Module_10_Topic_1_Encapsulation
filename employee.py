'''
Program: employee.py
Author: Joshua M. McGinley
Last date modified: 11/02/2022

Write your first class! Look at the Employee class above, copy and paste to employee.py in your IDE after you
create your Module10 project, class_definitions package and test package.
In designing code, we often use UML diagrams, below is the UML diagram for Employee class. In Python, it is less
obvious the type of data members. The - minus sign means private and the + plus sign means public. Use the
convention to consider private in naming your class variables in your constructor, do not use name mangling.
Note the examples above did not consider class data members private!
UML of Employee Class

The class attributes are the following:

last_name: string
first_name: string
address: string
phone_number: string
salaried: boolean
start_date: datetime
salary: float (sorry, had listed double as the type before, that is in C or Java; or Jython/CPython).

Methods:
display() returns a string that when printed will follow the below format:

Sasha Patel

123 Main Street

Urban, Iowa

Salaried employee: $40,000/year       # OR Hourly employee: $7.25/hour

Start date: 6-28-2019
Note this will have some logic statements to check for salaried or hourly to construct the return string.
'''

class Employee:
    def __init__(self, lname, fname, addy, pnumber, sala, startDate, sal_ary):
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = pnumber
        self.salaried = sala
        self.start_date = startDate #How would I set this using the datetime module?
        self.salary = sal_ary

    def __str__(self):
        if self.salaried == True:
            salary = 40000
            empPaid = 'Salaried employee: $40,000/year'
        else:
            salary = 7.25
            empPaid = 'Hourly employee: $7.25/hour'
        return str(self.first_name) + str(self.last_name) + '\n' + str(self.address) + '\n' + str(empPaid) + '\n' + str(self.start_date)

if __name__ == "__main__":
    emp1 = Employee('McGinley', 'Joshua ', '1212 8th St N\nNewnet, Iowa', '555-1212', False, 'Start date: 11-2-2022', '7.50')
    print(str(emp1))

