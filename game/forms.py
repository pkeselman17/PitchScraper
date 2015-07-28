from django import forms
from app.models import Sport

class CreateForm(forms.Form):
	sport = forms.ModelChoiceField(queryset= Sport.objects.all())
	latitude = forms.FloatField(widget=forms.HiddenInput())
	longitude = forms.FloatField(widget=forms.HiddenInput())
	description = forms.CharField(max_length=300)
	date = forms.DateTimeField(widget= forms.TextInput(attrs={
		'class':'datepicker'
	}))
	time = forms.DateTimeField(widget= forms.TextInput(attrs= {
		'class':'timepicker',
		'data-time-format':'h:i A'
	}))