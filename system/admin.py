from django.contrib import admin

# Register your models here.
from system.models import *

admin.site.register(Person)
admin.site.register(Profession)
admin.site.register(Task)