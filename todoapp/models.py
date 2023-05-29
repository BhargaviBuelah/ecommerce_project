from django.db import models
from todoapp.manager import Customclass

# Create your models here.
class Product(models.Model):#Applicationname_classname =>todoapp_product
    
    name=models.CharField(max_length=50)
    pdesc=models.CharField(max_length=100)
    price=models.FloatField()
    cat=models.CharField(max_length=10)
    is_deleted=models.CharField(max_length=5)
    uid=models.IntegerField()

    obj1=models.Manager()# changing name of the default object of manager class
    cobj1=Customclass() #custom class object

    def __str__(self):

        return self.name