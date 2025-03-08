from django.shortcuts import render
def indexPage(request):
    return render(request,"index.html")

def aboutPage(request):
    return render(request,"about.html")

def contactPage(request):
    return render(request,"contact.html")

def cropregistrationPage(request):
    return render(request,"cropregistration.html")

def healthcheckupPage(request):
    return render(request,"healthcheckup.html")

def marathiudyojakPage(request):
    return render(request,"marathiudyojak.html")