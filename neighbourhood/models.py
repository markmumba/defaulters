from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.


Priority=(
    ('Low Priority','Low Priority'),
    ('High Priority','High Priority'),
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
    contact = models.IntegerField()

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
    post = HTMLField()
    n_o_k_name = models.CharField(max_length=150)
    n_o_k_phone_number = models.CharField(max_length=12)
    neighbourhood= models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    house = models.ForeignKey(Business,on_delete=models.CASCADE,default=None)
    post_date = models.DateTimeField(auto_now_add=True)
    from_date = models.DateField()
    to_date = models.DateField()
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


    

class healthservices(models.Model):
    healthservices = models.CharField(max_length=100)

    def __str__(self):
        return self.healthservices

    def save_healthservices(self):
        self.save()

    @classmethod
    def delete_healthservices(cls,healthservices):
        cls.objects.filter(healthservices=healthservices).delete()

class Health(models.Model):
    logo = models.ImageField(upload_to='healthlogo/')
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)
    healthservices = models.ManyToManyField(healthservices)

    def __str__(self):
        return self.name


class Authorities(models.Model):
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class notifications(models.Model):
    title = models.CharField(max_length=100)
    notification = HTMLField()
    priority = models.CharField(max_length=15,choices=Priority,default="Informational")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


