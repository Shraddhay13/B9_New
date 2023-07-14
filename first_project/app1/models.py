from django.db import models

# Create your models here.

# tables -- columns --data types -- length --primary key

class Student(models.Model):
    # id -- django gives default id column -- primary key=True
    # below instance variables --no need to define constructor
    name = models.CharField(max_length=100)
    marks = models.IntegerField()
    address = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        # return f"{self.name} -- {self.address}"
        return f"{self.__dict__}"


    def show_detail(self):
        return f"""Name :- {self.name}
Marks:- {self.marks}
Address:- {self.address}
Age:- {self.age}
"""
    
    class Meta:  # nested class
        db_table = "student"

    def show_name_marks(self):
        return f"Name :- {self.name} -- Marks:-{self.marks}" 
    





#ORM - object relational mapper