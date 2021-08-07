from django import forms
from .models import applicant


class applicantForm(forms.ModelForm):
    class Meta:
        model = applicant
        fields = ['candidate_name','year','post']