from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
from .models import vehicle, centre, elder
# from .resources import elderResource
from django.contrib import messages
# from tablib import Dataset
from .forms import VehicleForm, CentreForm, ElderForm

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
def data(request):
    if request.method == 'POST':
        file = request.FILES['xlsxFile']
        csv = pd.read_csv(file)
        print(csv)

    template = loader.get_template('data.html')
    return HttpResponse(template.render())

def dataimport(request):
    
    template = loader.get_template('dataimport.html')
    return HttpResponse(template.render())

def upload(request):
    if request.method == 'POST' and request.FILES.get('xlsxFile'):
        xlsx_file = request.FILES['xlsxFile']
        df = pd.read_excel(xlsx_file)

        for _, row in df.iterrows():
            centre.objects.create(
                centre=row['centre'],
                cluster=row['cluster'],
                centrepostalcode=row['centrepostalcode']
            )

        for _, row in df.iterrows():
            elder.objects.create(
                elder=row['elder'],
                eldergender=row['eldergender'],
                nricorfin=row['nricorfin'],
                postalcode1=row['postalcode1'],
                postalcode2=row['postalcode2'],
                centre=row['centre'],
                tofromcentre=row['tofromcentre'],
                weekday=row['weekday'],
                etaetd=row['etaetd'],
                timepickupdeliver=row['timepickupdeliver'],
                eldertype=row['eldertype'],
                elderservicetype=row['elderservicetype'],
                caregiver=row['caregiver'],
                loadingtime=row['loadingtime'],
                rowid=row['rowid'],
                fromtopostal=row['fromtopostal'],
                distancekm=row['distancekm'],
                minn=row['minn'],
                min=row['min']
            )
        
        for _, row in df.iterrows():
            vehicle.objects.create(
                centre=row['centre'],
                tripid=row['tripid'],
                seqid=row['seqid'],
                vehicleplate=row['vehicleplate'],
                vehicletype=row['vehicletype'],
                vehiclecapacity=row['vehiclecapacity'],
                maxwheelchairelder=row['maxwheelchairelder'],
                maxambulantelder=row['maxambulantelder'],
                maxcaregiver=row['maxcaregiver']
            )
        
        headers = df.columns.tolist()
        rows = df.values.tolist()
        context = {
            'uploaded_file': True,
            'headers': headers,
            'rows': rows,
        }
    else:
        context = {'uploaded_file': False}

    return render(request, 'upload.html', context)

def database(request):
    if request.method == 'POST' and request.FILES.get('xlsxFile'):
        xlsx_file = request.FILES['xlsxFile']
        df = pd.read_excel(xlsx_file)
        
        for _, row in df.iterrows():
            centre.objects.create(
                centre=row['centre'],
                cluster=row['cluster'],
                centrepostalcode=row['centrepostalcode']
            )
        
        for _, row in df.iterrows():
            elder.objects.create(
                elder=row['elder'],
                eldergender=row['eldergender'],
                nricorfin=row['nricorfin'],
                postalcode1=row['postalcode1'],
                postalcode2=row['postalcode2'],
                centre=row['centre'],
                tofromcentre=row['tofromcentre'],
                weekday=row['weekday'],
                etaetd=row['etaetd'],
                timepickupdeliver=row['timepickupdeliver'],
                eldertype=row['eldertype'],
                elderservicetype=row['elderservicetype'],
                caregiver=row['caregiver'],
                loadingtime=row['loadingtime'],
                rowid=row['rowid'],
                fromtopostal=row['fromtopostal'],
                distancekm=row['distancekm'],
                minn=row['minn'],
                min=row['min']
            )
        
        for _, row in df.iterrows():
            vehicle.objects.create(
                centre=row['centre'],
                tripid=row['tripid'],
                seqid=row['seqid'],
                vehicleplate=row['vehicleplate'],
                vehicletype=row['vehicletype'],
                vehiclecapacity=row['vehiclecapacity'],
                maxwheelchairelder=row['maxwheelchairelder'],
                maxambulantelder=row['maxambulantelder'],
                maxcaregiver=row['maxcaregiver']
            )
        




# def upload(request):
#     if request.method == 'POST':
#         elder_resource = elderResource()
#         dataset = Dataset()
#         new_elder = request.FILES['xlsxFile']

#         if not new_elder.name.endswith('xlsx'):
#             messages.info(request,'wrong format')
#             return render(request,'dataimport.html')

#         imported_data = dataset.load(new_elder.read(),format='xlsx')
#         for data in imported_data:
#             value = elder(
#                 data[0],
#                 data[2],
#                 data[3],
#                 data[4],
#                 data[5],
#                 data[6],
#                 data[7],
#                 data[9],
#                 data[10],
#                 data[11],
#                 data[12],
#                 data[13],
#                 data[22],
#                 data[23],
#                 data[24],
#                 data[25],
#                 data[1],
#                 data[26],
#                 data[27],
#                 data[28],
#                 data[29]
#             )
#             value.save()
#         return render(request,'dataimport.html')

    
def dataexport(request):
    template = loader.get_template('dataexport.html')
    return HttpResponse(template.render())

def dataentry(request):
    template = loader.get_template('dataentry.html')
    return HttpResponse(template.render())

def elderinfo(request):
    if request.method == 'POST':
        form = ElderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data:elderinfo')
    else:
        form = ElderForm()
    return render(request, 'elderinfo.html', {'form': form})

def vehicleinfo(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data:vehicleinfo')
    else:
        form = VehicleForm()
    return render(request, 'vehicleinfo.html', {'form': form})

def centreinfo(request):

    form = CentreForm()

    if request.method == 'POST':
        form = CentreForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'centreinfo.html', context)



# def process_file(request):
#     if request.method == 'POST' and 'xlsx_file' in request.FILES:
#         xlsx_file = request.FILES['xlsx_file']
#         df = pd.read_excel(xlsx_file)

#         # Create elder objects
#         for _, row in df.iterrows():
#             elder_object = elder(
#                 elder=row['Elder'],
#                 eldergender=row['Elder Gender'],
#                 nricorfin=row['Elder NRIC or FIN Number'],
#                 postalcode1=row['Elder Postal code 1'],
#                 postalcode2=row['Elder Postal code 2'],
#                 centre=row['Centre'],
#                 tofromcentre=row['To/From Centre'],
#                 weekday=row['Weekday'],
#                 etaetd=row['ETA/ ETD'],
#                 timepickupdeliver=row['Time Pick-Up/ Deliver'],
#                 eldertype=row['Elder Type'],
#                 elderservicetype=row['Elder Service Type'],
#                 caregiver=row['Caregiver'],
#                 loadingtime=row['Loading Time'],
#                 rowid=row['row_id'],
#                 fromtopostal=row['FromToPostal'],
#                 distancekm=row['distance_km'],
#                 minn=row['min_n'],
#                 min=row['min (+svc time)']
#             )
#             elder_object.save()

#         # Create centre objects
#         for _, row in df.iterrows():
#             centre_object = centre(
#                 centre=row['Centre'],
#                 centreid=row['Centre ID'],
#                 cluster=row['Cluster'],
#                 centrepostalcode=row['Centre Postal Code']
#             )
#             centre_object.save()

#         # Create vehicle objects
#         for _, row in df.iterrows():
#             vehicle_object = vehicle(
#                 centre=row['Centre'],
#                 tripid=row['TRIP_ID'],
#                 seqid=row['SEQ_ID'],
#                 vehicleplate=row['Vehicle Plate'],
#                 vehicletype=row['Vehicle Type'],
#                 vehiclecapacity=row['Vehicle Capacity'],
#                 maxwheelchairelder=row['Max Number of Wheelchair Elder Assigned to Vehicle'],
#                 maxambulantelder=row['Max Number of Ambulant Elder Assigned to Vehicle'],
#                 maxcaregiver=row['Max Number of Caregiver Assigned to Vehicle']
#             )
#             vehicle_object.save()

#         return render(request, 'dataimport.html')

        
    

   

    




