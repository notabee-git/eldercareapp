from django.db import models

class vehicle(models.Model):
  centre = models.CharField(max_length=255)
  tripid = models.IntegerField() # TRIP_ID
  seqid = models.IntegerField() #SEQ_ID
  vehicleplate = models.CharField(max_length=255) #Vehicle Plate
  vehicletype = models.CharField(max_length=255)
  vehicleid = models.IntegerField()
  vehiclecapacity = models.IntegerField()
  maxwheelchairelder = models.IntegerField()
  maxambulantelder = models.IntegerField()
  maxcaregiver = models.IntegerField()

class centre(models.Model):
  centre = models.CharField(max_length=255)
  centreid = models.IntegerField()
  cluster = models.CharField(max_length=255)
  centrepostalcode = models.IntegerField()
    

class elder(models.Model):
  elder = models.IntegerField()
  eldergender = models.CharField(max_length=255)
  elderid = models.IntegerField()
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
  rowid = models.IntegerField(null=True) # row_id : (extra info added so keeping them NULL)
  fromtopostal = models.IntegerField(null=True) #  FromToPostal : null
  distancekm = models.IntegerField(null=True) # distance_km null
  minn = models.IntegerField(null=True) # min_n : null
  min = models.IntegerField(null=True) # min (+svc time): null




