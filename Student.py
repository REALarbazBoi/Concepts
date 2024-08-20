class Student:
    def __init__(self,roll,name,dept):
        self.roll = roll
        self.name = name
        self.dept = dept
    
    def display(self):
        print(f"Roll no: {self.roll} \nName: {self.name} \ndept: {self.dept}")