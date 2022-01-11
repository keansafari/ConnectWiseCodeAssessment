class Person:
    def __init__(self, name, age, gender, city, state, student, employee):
        self.name = name
        self.age = age
        self.gender = gender
        self.city = city
        self.state = state
        self.student = student
        self.employee = employee

    def GetPerson(self):
        if len(self.name) > 0 and len(self.city) > 0 and len(self.student) > 0 and len(self.gender) > 0 and len(self.employee) > 0:
            if len(self.age) < 1:
                return f'{self.name} [{self.gender}]\n\tCity : {self.city}\n\tState : {self.state}\n\tStudent : {self.student}\n\tEmployee : {self.employee}'    
            if len(self.gender) < 1:
                return f'{self.name} [{self.age}]\n\tCity : {self.city}\n\tState : {self.state}\n\tStudent : {self.student}\n\tEmployee : {self.employee}'
            return f'{self.name} [{self.age}, {self.gender}]\n\tCity : {self.city}\n\tState : {self.state}\n\tStudent : {self.student}\n\tEmployee : {self.employee}'
        else:
            return 'Invalid data, unable to process'