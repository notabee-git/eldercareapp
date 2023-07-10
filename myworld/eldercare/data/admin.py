from django.contrib import admin
from .models import elder,vehicle,centre
# from import_export.admin import ImportExportModelAdmin


# @admin.register(elder)
# class elderAdmin(ImportExportModelAdmin):
#     list_display = ('eldergender', 'elderid', 'nricorfin', 'postalcode1', 'postalcode2', 'centre', 'tofromcentre', 'weekday', 'etaetd', 'timepickupdeliver', 'eldertype', 'elderservicetype', 'caregiver',   'loadingtime', 'rowid', 'fromtopostal', 'distancekm', 'minn','min')


admin.site.register(elder)
admin.site.register(vehicle)
admin.site.register(centre)

