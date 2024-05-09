from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    age = models.IntegerField()
    phone = models.CharField(max_length=9)

    def __str__(self):
        return self.name + ' ' + self.last_name
    
class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.name