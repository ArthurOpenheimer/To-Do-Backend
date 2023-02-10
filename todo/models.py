from django.db import models

class User(models.Model):
    username= models.CharField(max_length=100, db_column='username')
    password= models.CharField(max_length=100, db_column='password')
    
    def __str__(self):
        return self.username

class Todo(models.Model):
    name= models.CharField(max_length=100)
    user= models.ForeignKey(User, on_delete=models.CASCADE, default='')
    
    def __str__(self):
        return self.name
    
    