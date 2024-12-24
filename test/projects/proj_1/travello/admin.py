from django.contrib import admin
from .models import Destination    # Make sure the model name has the correct capitalization

# Register your models here.
admin.site.register(Destination  )  # Use 'site' (singular) and ensure the model name matches the one in models.py
                                                         