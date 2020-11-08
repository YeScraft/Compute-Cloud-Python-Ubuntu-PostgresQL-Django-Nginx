from django.contrib import admin
from .models import Cars
# Register your models here.
@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model', 'year')

    def save_model(self, request, obj, form, change):
        obj.mark = obj.mark.lower()
        obj.model = obj.model.lower()
        obj.color = obj.color.lower()
        super().save_model(request, obj, form, change)