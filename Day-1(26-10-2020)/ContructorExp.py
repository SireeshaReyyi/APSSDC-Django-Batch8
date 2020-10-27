class student:
    def __init__(self,name,rollno,email):
        self.name=name
        self.rollno=rollno
        self.email=email

    def show(self):
        return {"Name":self.name,'Rollno':self.rollno,
                'EMAIL':self.email}
    
        
        
        
