from django.db import models
from User.models import *



    

    #create order table for save a order
class Order(models.Model):
    item = models.CharField(max_length = 255)
    quentity = models.IntegerField()
    address= models.CharField(max_length=400)
    contact = models.CharField(max_length=50)
    date =models.DateField(max_length=50)
    username=models.CharField(max_length=40)
    userid  =  models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)

    
class Food(models.Model):
    foodname = models.CharField(max_length = 255)
    foodprice = models.IntegerField()
    foodimage = models.ImageField(upload_to='images/')




