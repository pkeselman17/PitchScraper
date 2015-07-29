from django import forms
from app.models import Sport

class CreateForm(forms.Form):
	sport = forms.ModelChoiceField(queryset= Sport.objects.all())
	latitude = forms.FloatField(label= "Location", widget=forms.HiddenInput())
	longitude = forms.FloatField(widget=forms.HiddenInput(), required=False)
	description = forms.CharField(max_length=300)
	date = forms.DateTimeField(widget= forms.TextInput(attrs={
		'class':'datepicker'
	}))
	time = forms.CharField(widget= forms.TextInput(attrs= {
		'id':'timeField',
		'data-time-format':'h:i A'
	}))
	