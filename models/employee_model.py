from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    address=models.TextField()        
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    
