from django.forms import ModelForm
from .models import Member

class Memberform(ModelForm):
    class Meta:
        model = Member
        fields = ['fname', 'lname', 'email', 'passwd', 'age']