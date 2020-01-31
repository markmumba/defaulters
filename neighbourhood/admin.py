from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile);
admin.site.register(neighbourhood);
admin.site.register(defaulter);
admin.site.register(Business);
admin.site.register(notifications);