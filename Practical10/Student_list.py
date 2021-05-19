class Student():
    def __init__(self,first_name,last_name,undergraduate_programme):
        self.first_name=first_name
        self.last_name=last_name
        self.undergraduate_programme=undergraduate_programme

    def information(self):
        print(self.first_name.title()+' '+self.last_name.title()+': '+self.undergraduate_programme)
student=Student('zihan','chu','BMS')
student.information()
