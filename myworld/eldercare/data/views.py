from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import vehicle, centre, elder

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
def data(request):
    template = loader.get_template('data.html')
    return HttpResponse(template.render())

def dataimport(request):
    template = loader.get_template('dataimport.html')
    return HttpResponse(template.render())
    
def dataexport(request):
    template = loader.get_template('dataexport.html')
    return HttpResponse(template.render())

def dataentry(request):
    template = loader.get_template('dataentry.html')
    return HttpResponse(template.render())

def process_file(request):
    if request.method == 'POST' and 'xlsx_file' in request.FILES:
        xlsx_file = request.FILES['xlsx_file']
        df = pd.read_excel(xlsx_file)

        # Create elder objects
        for _, row in df.iterrows():
            elder_object = elder(
                elder=row['Elder'],
                eldergender=row['Elder Gender'],
                nricorfin=row['Elder NRIC or FIN Number'],
                postalcode1=row['Elder Postal code 1'],
                postalcode2=row['Elder Postal code 2'],
                centre=row['Centre'],
                tofromcentre=row['To/From Centre'],
                weekday=row['Weekday'],
                etaetd=row['ETA/ ETD'],
                timepickupdeliver=row['Time Pick-Up/ Deliver'],
                eldertype=row['Elder Type'],
                elderservicetype=row['Elder Service Type'],
                caregiver=row['Caregiver'],
                loadingtime=row['Loading Time'],
                rowid=row['row_id'],
                fromtopostal=row['FromToPostal'],
                distancekm=row['distance_km'],
                minn=row['min_n'],
                min=row['min (+svc time)']
            )
            elder_object.save()

        # Create centre objects
        for _, row in df.iterrows():
            centre_object = centre(
                centre=row['Centre'],
                centreid=row['Centre ID'],
                cluster=row['Cluster'],
                centrepostalcode=row['Centre Postal Code']
            )
            centre_object.save()

        # Create vehicle objects
        for _, row in df.iterrows():
            vehicle_object = vehicle(
                centre=row['Centre'],
                tripid=row['TRIP_ID'],
                seqid=row['SEQ_ID'],
                vehicleplate=row['Vehicle Plate'],
                vehicletype=row['Vehicle Type'],
                vehiclecapacity=row['Vehicle Capacity'],
                maxwheelchairelder=row['Max Number of Wheelchair Elder Assigned to Vehicle'],
                maxambulantelder=row['Max Number of Ambulant Elder Assigned to Vehicle'],
                maxcaregiver=row['Max Number of Caregiver Assigned to Vehicle']
            )
            vehicle_object.save()

        return render(request, 'dataimport.html')

        
    

   

    




