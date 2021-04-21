from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
def fac_register(request):
    return render(request,"faculty/fac_register.html")
def registration(request):
    name=request.POST.get("name")
    email=request.POST.get("email")
    course=request.POST.get("course")
    experience=request.POST.get("exp")
    print(name,email,course,experience)
    return render(request,"faculty/fac_register.html")
def faculty_login(request):
    return render(request,"faculty/fac_login.html")
def log_in(request):
    username=request.POST.get("username")
    password= request.POST.get("password")
    print(username,password)
    return render(request,"faculty/faclogged.html")
def view_schedule(request):
    return HttpResponse("<h1>welcome to schedule page</h1>")
def view_feedback(request):
    return HttpResponse("<h1>welcome to feedback page</h1>")



