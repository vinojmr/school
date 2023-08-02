from django.contrib import admin
from . models import Department, Course, Country, District, State

# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)