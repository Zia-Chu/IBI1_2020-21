class Student():
# initialise the arguments
    def __init__(self,first_name,last_name,undergraduate_programme):
# get the value of arguments
        self.first_name=first_name
        self.last_name=last_name
        self.undergraduate_programme=undergraduate_programme
#print full name and undergraduate programme
    def information(self):
        print(self.first_name.title()+' '+self.last_name.title()+': '+self.undergraduate_programme) # turn the name in capitals
# example        
student=Student('zihan','chu','BMS')
student.information()
