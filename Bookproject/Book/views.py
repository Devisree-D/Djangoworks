from django.shortcuts import render

# Create your views here.
from .forms import BookcreateForm,UserRegisterForm,LoginForm
from django.shortcuts import render,redirect
from .models import Book
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy
def book_create(request):
    form=BookcreateForm()
    context={}
    context["form"]=form
    books=Book.objects.all()
    context["books"]=books
    if request.method == "POST":
        form = BookcreateForm(request.POST)
        if form.is_valid():
            form.save()
            print("Book saved")
            return redirect("create")
        else:
            form = BookcreateForm(request.POST)
            context["form"] = form
            return render(request, "book/bookcreate.html", context)


    return render(request, "book/bookcreate.html", context)

def book_view(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request, "book/book_detail.html", context)
def book_update(request,id):
    book=Book.objects.get(id=id)
    form=BookcreateForm(instance=book)
    context={}
    context["form"]=form
    if request.method=='POST':
        form=BookcreateForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("create")
    return render(request, "book/book_update.html", context)

def book_delete(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("create")

def registration(request):
    form=UserRegisterForm()
    context={}
    context["form"]=form

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "book/userlogin.html")
        else:
            form = UserRegisterForm(request.POST)
            context["form"] = form
            return render(request, "book/registration.html", context)
    return render(request, "book/registration.html", context)


def login_view(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                print("login success")
                login(request,user)
                return redirect("create")
            else:
                print("login failed")
                return render(request, "book/userlogin.html", context)

    return render(request, "book/userlogin.html",context)
def log_out(request):
    logout(request)
    form = LoginForm()
    context = {}
    context["form"] = form
    return render(request, "book/userlogin.html",context)

class Books(ListView):
    model = Book
    template_name = "book/bookcreate.html"
    # context={}  #only model and template is given and by default django gives all functions
    # books=Book.objects.all()
    # context["object_list"]=books

class BookCreate(CreateView):
    model = Book
    form_class = BookcreateForm
    template_name = "book/bookcreate.html"
    success_url = reverse_lazy("clslist")
class BookUpdate(UpdateView):
    model = Book
    form_class = BookcreateForm
    template_name = "book/book_update.html"
    success_url = reverse_lazy("clslist")

class BookDetail(DetailView):
    model=Book
    template_name = "book/book_detail.html"


class Bookdelete(DeleteView):
    model = Book
    template_name = "book/bookdelete.html"
    success_url = reverse_lazy("clslist")







