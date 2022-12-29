from django.contrib import admin

# Import models in current application folder
from .models import Yoga

# Register your models here.

# Register yoga model in admin panel
admin.site.register(Yoga)


