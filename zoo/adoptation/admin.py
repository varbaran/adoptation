from django.contrib import admin
from .models import Dog,Cat,Adopter
# Register your models here.
admin.site.register(Dog)
admin.site.register(Cat)
admin.site.register(Adopter)