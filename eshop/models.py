from django.db import models

# Create your models here.


class Ussr(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.fname

class Category(models.Model):
    cname = models.CharField(max_length=50)
    cimg = models.CharField(max_length=50,blank=True)
    ccount = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.cname

class Product(models.Model):
    pname = models.CharField(max_length=100)
    pdesc = models.TextField(blank=True)
    pslug = models.CharField(max_length=100,blank=True)    
    pprice = models.CharField(max_length=100,blank=True)
    pimg = models.CharField(max_length=100,blank=True)
    pcat = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    