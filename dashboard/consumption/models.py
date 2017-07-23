# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

# The Summary model is for loading the processed summary data from load.py
class Summary(models.Model):
    summary_time=models.DateTimeField()
    summary_use=models.FloatField()
	#This is for having readable output
    def __str__(self):
        output=+str(self.summary_time)+", "+str(self.summary_use)  
        return output
    
# The User model is for loading the data from /data/user_data.csv
class User(models.Model):
    user_id=models.IntegerField()
    user_area=models.CharField(max_length=2)
    user_tariff=models.CharField(max_length=2)
    def __str__(self):
        output=str(self.user_id)+", "+self.user_area+", "+self.user_tariff
        return output

#The EnergyUse model is linked with the User model for loading data from the user files from /data/consumption
class EnergyUse(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) #This links the EnergyUse with the User model
    EnergyUse_time=models.DateTimeField()
    EnergyUse_consumption=models.FloatField()
    def __str__(self):
        output=str(self.user_id)+", "+str(self.EnergyUse_time)+", "+str(self.EnergyUse_consumption)  
        return output
        
