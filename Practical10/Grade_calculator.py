class Grade():
    def __init__(self,first_name,last_name,portfolio_grade,poster_grade,exam_grade,final):
        self.first_name = first_name
        self.last_name = last_name
        self.portfolio_grade = portfolio_grade
        self.poster_grade=poster_grade
        self.exam_grade=exam_grade
        self.final=final

    def caculate(self):
        final=self.portfolio_grade*0.4 + self.exam_grade*0.3 + self.poster_grade*0.3
        print(self.first_name.title()+' ',self.last_name.title(),': ',final)

final_grade=Grade('zihan','chu',90,80,88,0)
final_grade.caculate()
