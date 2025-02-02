from django.db import models

# Create your models here.
class books(models.Model):
    bookid=models.CharField(max_length=50)
    bname=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    quantity=models.IntegerField()
    
    class Meta:
        db_table="books"

class student(models.Model):
    s_id=models.CharField(max_length=50)
    sname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    
    class Meta:
        db_table="student"

class issue(models.Model):
    s_id=models.CharField(max_length=50)
    b_id=models.CharField(max_length=50)
    i_date=models.DateField()
    r_date=models.DateField(null=True,blank=True)
    fine=models.IntegerField(default=0)

    class Meta:
        db_table="issue"

class login(models.Model):
    a_id = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)

    class Meta:
        db_table="login"

