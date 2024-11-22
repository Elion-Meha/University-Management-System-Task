class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def set_details(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self,name,age,gender):
        print(f"Name: {self.name}, Age: {self.age} Gender: {self.gender}")



class student(person):
    def __init__(self, name, age, gender):
        super().__init__(self, name, age, gender):
        self.id = none 
        self.course = none 
        self.grades []

    def set_student_details    

        

