from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    description = models.TextField()
    contacted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    img = models.ImageField(upload_to='blog',blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Details(models.Model):
    title = models.TextField()
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    degree = models.CharField(max_length=50)
    email = models.EmailField()
    freelance = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
    
class Skills(models.Model):
    fields = models.CharField(max_length=50)
    desc = models.TextField()
    level = models.IntegerField() 
    image = models.ImageField(upload_to='media',blank=True, null=True,)

    def __str__(self):
        return self.fields