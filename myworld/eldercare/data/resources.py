from import_export import resources
from .models import elder 

class elderResource(resources.ModelResource):
    class meta:
        model = elder