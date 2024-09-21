from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout

# Create your views here.
def register_view(request):
    if request == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return 'success'
    else:
        form = UserCreationForm()
    return render(request, 'register.html',{'form':form})

        
    

def login_view(request):
    pass

def dashboard(request):
    pass

def logout_view(request):
    pass