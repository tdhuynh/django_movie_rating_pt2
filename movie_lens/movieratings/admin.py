from django.contrib import admin
from movieratings.models import Item, Rater, Data

# Register your models here.
admin.site.register([Item, Rater, Data])
