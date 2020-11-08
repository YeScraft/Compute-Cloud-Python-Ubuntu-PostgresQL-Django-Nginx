from django import forms

from .models import Cars


class MarkModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s"%obj.mark


class ModelModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s"%obj.model


class YearModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s"%obj.year


class ColorModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s"%obj.color


class CarsForm(forms.Form):
    GEAR_CHOICES = [
        (None, '---------'),
        (1, 'механика'),
        (2, 'автомат'),
        (3, 'робот')
    ]

    mark = MarkModelChoiceField(label="mark", queryset=Cars.objects.order_by('mark'), required=False)
    model = ModelModelChoiceField(label="model", queryset=Cars.objects.order_by('model'), required=False)
    year = YearModelChoiceField(label="year", queryset=Cars.objects.order_by('-year'), required=False)
    gear = forms.ChoiceField(label='cars_gear', choices=GEAR_CHOICES, required=False, initial=None)
    color = ColorModelChoiceField(label="color", queryset=Cars.objects.order_by('color'), required=False)

    mark.widget.attrs.update({'class': 'form-control'})
    model.widget.attrs.update({'class': 'form-control'})
    year.widget.attrs.update({'class': 'form-control'})
    gear.widget.attrs.update({'class': 'form-control'})
    color.widget.attrs.update({'class': 'form-control'})
