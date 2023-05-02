from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(primary_key=True, max_length=100)
    uemail = models.EmailField()
    time_taken = models.CharField(max_length=100)
    class Meta:
        #managed = False
        db_table = 'user'

class treasure(models.Model):
    username=models.CharField(primary_key=True, max_length=100)
    useremail=models.EmailField()
    status=models.CharField(max_length=50)
    class Meta:
        db_table= 'treasure'
