from django.shortcuts import render
from .models import Member

def home(request):
#   This is will sign everything that is in our database into this variable...
    all_members = Member.objects.all
    return render(request, 'home.html', {'all' : all_members})

# Creating join, we will integrate our web page with our database here...
def join(request):
    return render(request, 'join.html', {})