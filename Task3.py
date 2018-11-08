

class Person:
    def __init__ (self,name,surname,date_of_birth,adress):
        self.name = name
        self.surname=surname
        self.date_of_birth = date_of_birth
        self.adress = adress

    def Predstavljanje(self):
            print("My name is {0} {1}. My surname is {2}.".format(self.name, self.surname))

    def __str__(self):
            return self.name + " " + self.surname





class Employee (Person):
    def __init__ (self,company,position,years_employed,base_salary):
        self.company = company
        self.position = position
        self.years_employed = years_employed
        self.base_salary = base_salary

    def __str__(self):
        return  self.company + " " + self.position



class Freelancer(Person):
    def __init__ (self,skills,reviews):



































