from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClientForm
#create your views here
def client_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return redirect('client')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ClientForm()
    return render(request, 'Laswo/client.html', {'form': form})

def home_view(request):
    return render(request, 'Laswo/home.html')

def photo_view(request):
    return render(request, 'Laswo/photos.html')

def service_view(request):
    return render(request, 'Laswo/service.html')

def about_view(request):
    return render(request, 'Laswo/about.html')

def contact_view(request):
    return render(request, 'Laswo/contact.html')

