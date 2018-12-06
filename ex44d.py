# This is creating a class "Parent" as an object
class Parent(object):
    
    # Each def will cause the functions to either override the object class, implicit the object class, and alter the object class
    def override(self):
        print("PARENT override()")
    
    def implicit(self):
        print("PARENT implicit()")
    
    def altered(self):
        print("PARENT altered()")

# This is creating a class "Child" as another object
class Child(Parent):
    
    # Now this will either override the object class and alter the object class
    def override(self):
        print("CHILD override()")
    
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        #Super in Python means that it returns a proxy object to delegate method calls to a class, in this case the parent and child class object
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

# each variable is being assigned to their proper classes
dad = Parent()
son = Child()

# The variables are being implicited by their respective classes
dad.implicit()
son.implicit()

# the variables are being overridden by their respective classes
dad.override()
son.override()

# the variables are being altered by their respective classes
dad.altered()
son.altered()
