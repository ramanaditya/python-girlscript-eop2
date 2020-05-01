"""
attribute
A variable that is part of a class.

class
A template that can be used to construct an object.
Defines the attributes and methods that will make up the object.

child class
A new class created when a parent class is extended.
The child class inherits all of the attributes and methods of the
parent class.

constructor
An optional specially named method (__init__) that is called at
the moment when a class is being used to construct an
object. Usually this is used to set up initial values for the object.

destructor
An optional specially named method (__del__) that is called at
the moment just before an object is destroyed.
Destructors are rarely used.

inheritance
When we create a new class (child) by extending an existing class
(parent). The child class has all the attributes and
methods of the parent class plus additional attributes and
methods defined by the child class.

method
A function that is contained within a class and the objects that are constructed from the class. Some object-oriented
patterns use 'message' instead of 'method' to describe this concept.

object
A constructed instance of a class. An object contains all of the attributes and methods that were defined by the class.
 Some object-oriented documentation uses the term 'instance' interchangeably with 'object'.

parent class
The class which is being extended to create a new child class. The parent class contributes all of its methods and
attributes to the new child class.
"""


"""
Defining the class
"""


class Profile:
    """Class Definition"""

    """Attributes"""
    college_name = "XYZ COllege"
    name = ""
    teacher = ""
    total_marks = 0.0
    percentage = 0.0

    def __init__(self, name,username, branch=None):
        """Constructor"""
        self.name = name
        self.branch = branch
        self.__username = username
        print("Profile of student : {0} has been created in the branch : {1}".format(self.name,self.branch))

    def teacher_fun(self,teacher):
        self.teacher = teacher
        print("Student : {0} is associated with teacher : {1}".format(self.name, self.teacher))

    def provide_marks(self, english= None,computer=None,network = None):
        marks_obtained = 0
        total_marks = 0
        if english:
            marks_obtained += english
            total_marks += 100
        if computer:
            marks_obtained += computer
            total_marks += 100
        if network:
            marks_obtained += network
            total_marks += 100

        self.total_marks = marks_obtained
        per = (marks_obtained/total_marks)*100
        print("Percentage of student {} is {}".format(self.name,per))

    @classmethod
    def print_details(cls):
        print(cls.college_name)
        return cls.college_name

    @staticmethod
    def feedback(feedback):
        print(feedback)

    def __del__(self):
        """Destructor"""
        print("The profile of Student : {0} and branch : {1} has now been deleted".format(self.name,self.branch))


if __name__ == "__main__":
    s1 = Profile("Aditya","aditya","CSE")
    s2 = Profile("Raman" , "raman" , "ME")
