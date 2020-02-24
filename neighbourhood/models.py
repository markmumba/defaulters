from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.


Kintype=(
    ('Wife','Wife'),
    ('Husband','Husband'),
    ('Son','Son'),
    ('Daughter','Daughter'),
    ('Mother','Mother'),
    ('Father','Father'),
    ('Other','Other')
)

class neighbourhood(models.Model):
    neighbourhood= models.CharField(max_length=100)

    def __str__(self):
        return self.neighbourhood

    def create_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(neighbourhood=neighbourhood).delete()



class Profile(models.Model):
    profpic = models.ImageField(upload_to='profpics/')
    description = HTMLField()
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
class Business(models.Model):
    logo = models.ImageField(upload_to='logos/')
    description = HTMLField()
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    address =models.CharField(max_length=100)
    contact = models.CharField(max_length=12)

    def __str__(self):
        return self.name
    
    @classmethod
    def search_business(cls,search_term):
        businesses = cls.objects.filter(description__icontains=search_term)
        return businesses

class defaulter(models.Model):
    name = models.CharField(max_length=150)
    id_number = models.CharField(max_length=12)
    image = models.ImageField(upload_to='post/')
    phone_number = models.CharField(max_length=12)
    comments = models.CharField(max_length=150,default=None)
    Next_Of_Kin_Name = models.CharField(max_length=150,default=None)
    Next_Of_Kin_Relationship = models.CharField(max_length=15,choices=Kintype,default="Wife")
    Next_Of_Kin_Phone_Number = models.CharField(max_length=12,default=None)
    neighbourhood= models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    house = models.ForeignKey(Business,on_delete=models.CASCADE,default=None)
    post_date = models.DateTimeField(auto_now_add=True)
    from_date = models.DateField()
    to_date = models.DateField()
    amount =models.CharField(max_length=1000,default=None)
    email_address = models.EmailField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    @classmethod
    def search_defaulter(cls,search_term):
        defaulters = cls.objects.filter(id_number__icontains=search_term)
        return defaulters

class Comment(models.Model):
    comment = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(defaulter,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

