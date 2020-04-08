class Student:
    
    def __init__(self, name, avg, level):
        self.name = name
        self.avg = avg
        self.level = level
        
    def tell_about_yourself(self):
        print("My namd is " + self.name)
        
        

ahmad = Student("ahmad", 18.5, 8)
ahmad.tell_about_yourself()