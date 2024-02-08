from django.db import models
#create ur class here


class Staff(models.Model):
    Staff_name= models.CharField(max_length=20)
    Contact = models.CharField(max_length=20)
    Gender_choices= [
        ('Male','Male'),
        ('Female','Female')
    ]
    Gender = models.CharField(choices= Gender_choices,default='Male',max_length=20)
    Date_Employed= models.DateField(auto_now=True)

class Department(models.Model):
    Dept_name = models.CharField(max_length = 25)
    Staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
   
   

class Courses(models.Model):
    course_Name = models.CharField(max_length=10)
    course_code = models.CharField(max_length=10)
    Dept_name = models.ForeignKey(Department,on_delete=models.CASCADE)

class Course_unit(models.Model):
    Unit_Name =models.CharField(max_length=25)
    Unit_Code=models.CharField(max_length=20)
    courses= models.ForeignKey(Courses,on_delete=models.CASCADE)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE)
    Staff = models.ForeignKey(Staff,on_delete=models.CASCADE)


class Student(models.Model):
    Name = models.CharField(max_length=30)
    Reg_No=models.CharField(max_length=30, unique=True)
    Student_Email=models.CharField(max_length=30)
    Student_Number=models.CharField(max_length=30)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE)
    Courses=models.ForeignKey(Courses,on_delete=models.CASCADE)
