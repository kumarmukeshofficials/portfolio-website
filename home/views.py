from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    return render(request,'home.html')    
        
def about(request):
    return render(request,'about.html') 

def portfolio(request):
    return render(request,'portfolio.html')


def contact(request):
    if request.method=="POST":
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        desc= request.POST['desc']
        print(name,email,phone,desc)
        ins = Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
        print("thsi data has been written into db")


    return render(request,'contact.html') 
    
    