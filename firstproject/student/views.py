from django.http import HttpResponse


# Create your views here.

from django.shortcuts import render,redirect
from student.models import Studentreg
from student.forms import StudentRegistrationform, Studentloginpage
def registration(request):
    form=StudentRegistrationform()
    context={}
    context["form"]=form
    studs = Studentreg.objects.all()
    context["studs"] = studs
    if (request.method=='POST'):
        form=StudentRegistrationform(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get("name")
            email=form.cleaned_data.get("email")
            phone=form.cleaned_data.get("phone")
            course=form.cleaned_data.get("course")
            username=form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            stud=Studentreg(name=name,email=email,phone=phone,course=course,username=username,password=password)
            stud.save()
            print("student registered")
            return redirect("register")
    return render(request,"student/studentRegistration.html",context)
def stud_delete(request,id):
    stud=Studentreg.objects.get(id=id)
    stud.delete()
    return redirect("register")
def loginpage(request):
    form=Studentloginpage()
    context={}
    context["form"]=form

    if (request.method=='POST'):
        form=Studentloginpage(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            print(username,"==>",password)
            return render(request, "student/studentlogin.html", context)
    return render(request,"student/studentlogin.html",context)




# def stud_register(request):
#     return render(request,"student/stud_register.html")
# def registration(request):
#     name=request.POST.get("name")
#     email=request.POST.get("email")
#     course=request.POST.get("course")
#     print(name,email,course)
#     return render(request,"student/stud_register.html")
# def student_login(request):
#     return render(request,"student/stud_login.html")
# def log_in(request):
#     username=request.POST.get("username")
#     password=request.POST.get("password")
#     print(username,password)
#     return render(request,"student/logged.html")
# def view_timetable(request):
#     return render(request,"student/timetable.html")
# def post_feedback(request):
#     return render(request,"student/stud_feedback.html")
# def stud_fb(request):
#     student=request.POST.get("stud")
#     faculty=request.POST.get("fac")
#     feedback=request.POST.get("fb")
#     print(student,faculty,feedback)
#     return render(request,"student/stud_feedback.html")
