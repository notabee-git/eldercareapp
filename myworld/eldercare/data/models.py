from django.db import models

class vehicle(models.Model):
  centre = models.CharField(max_length=255)
  driverid = models.IntegerField() # trip id
  drivername = models.CharField(max_length=255, null=True) #missing in input data so keeping NULL
  vehicleno = models.IntegerField() #seq id
  vehicleid = models.CharField(max_length=255) #vehicle plate
  vehicletype = models.CharField(max_length=255)
  vehiclecapacity = models.IntegerField()
  maxwheelchairelder = models.IntegerField()
  maxambulantelder = models.IntegerField()
  maxcaregiver = models.IntegerField()

class centre(models.Model):
  centre = models.CharField(max_length=255)
  centreid = models.IntegerField()
  clusterid = models.IntegerField()
  centrepostalcode = models.IntegerField()
    

class elder(models.Model):
  elder = models.IntegerField()
  eldergender = models.CharField(max_length=255)
  nricorfin = models.CharField(max_length=255)
  postalcode1 = models.IntegerField()
  postalcode2 = models.CharField(max_length=255)
  centre = models.CharField(max_length=255)
  tofromcentre = models.CharField(max_length=255)
  weekday = models.CharField(max_length=255)
  etaetd = models.IntegerField()
  timepickupdeliver = models.IntegerField()
  eldertype = models.CharField(max_length=255)
  elderservicetype = models.CharField(max_length=255)
  caregiver = models.IntegerField()
  loadingtime = models.IntegerField()
  rowid = models.IntegerField(null=True) #extra info added so keeping them NULL
  fromtopostal = models.IntegerField(null=True) # null
  distancekm = models.IntegerField(null=True) #null
  minn = models.IntegerField(null=True) #null
  min = models.IntegerField(null=True) #null




