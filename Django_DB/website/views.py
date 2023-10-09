from django.shortcuts import render, redirect
from .models import Member
from .forms import Memberform
from django.contrib import messages

def home(request):
#   This is will sign everything that is in our database into this variable...
    all_members = Member.objects.all
    context = {'all' : all_members}
    return render(request, 'home.html', context)

# Creating join, we will integrate our web page with our database here...
def join(request):
    if request.method == 'POST':
        form = Memberform(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Form Submitted!'))
        return redirect('home')        
    else:
        return render(request, 'join.html', {})