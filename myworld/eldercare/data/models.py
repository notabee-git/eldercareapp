from django.db import models

class vehicle(models.Model):
  centre = models.CharField(max_length=255)
  tripid = models.CharField(max_length=255) # TRIP_ID
  seqid = models.CharField(max_length=255) #SEQ_ID
  vehicleplate = models.CharField(max_length=255) #Vehicle Plate
  vehicletype = models.CharField(max_length=255)
  # vehicleid = models.CharField(max_length=255)
  vehiclecapacity = models.CharField(max_length=255)
  maxwheelchairelder = models.CharField(max_length=255)
  maxambulantelder = models.CharField(max_length=255)
  maxcaregiver = models.CharField(max_length=255)

class centre(models.Model):
  centre = models.CharField(max_length=255)
  # centreid = models.CharField(max_length=255)
  cluster = models.CharField(max_length=255)
  centrepostalcode = models.CharField(max_length=255)
    

class elder(models.Model):
  elder = models.CharField(max_length=255)
  eldergender = models.CharField(max_length=255)
  nricorfin = models.CharField(max_length=255)
  postalcode1 = models.CharField(max_length=255)
  postalcode2 = models.CharField(max_length=255)
  centre = models.CharField(max_length=255)
  tofromcentre = models.CharField(max_length=255)
  weekday = models.CharField(max_length=255)
  etaetd = models.CharField(max_length=255)
  timepickupdeliver = models.CharField(max_length=255)
  eldertype = models.CharField(max_length=255)
  elderservicetype = models.CharField(max_length=255)
  caregiver = models.CharField(max_length=255)
  loadingtime = models.CharField(max_length=255)
  rowid = models.CharField(max_length=255) # row_id : (extra info added so keeping them NULL)
  fromtopostal =models.CharField(max_length=255) #  FromToPostal : null
  distancekm = models.CharField(max_length=255) # distance_km null
  minn = models.CharField(max_length=255) # min_n : null
  min = models.CharField(max_length=255) # min (+svc time): null



