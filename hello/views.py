# editing view.py file
from django.shortcuts import render, HttpResponse
#import django.http from HttpResponse
from helloworld.models import Contact
from django.contrib import messages

def index(request):
      return render(request, 'index.html')
      #return render(request, 'index.html',context)
      #return HttpResponse("Hello World!")

def about(request):
      return render(request, 'about.html')
      #return HttpResponse("About page")

def services(request):
      return render(request, 'services.html')
      #return HttpResponse("Services!")

def contact(request):
      if request.method == "POST":
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            email = request.POST.get('email')
            desc = request.POST.get('desc')
            city = request.POST.get('city')
            contact = Contact(name=name, surname=surname, email=email, desc=desc, city=city)
            contact.save()    
            messages.success(request, 'Your Message Has Been Sent. Thank You!')

      return render(request, 'contact.html')
      #return HttpResponse("Contacts page!")
