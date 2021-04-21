from django.shortcuts import render,redirect
from  .forms import BrandcreateForm,MobilecreateForm,UserRegisterForm,UserpurchaseForm
from .models import Mobile,Brands,Myorders
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def admin_permission_requied(func):
    def inner(request):
        if not request.user.is_superuser:
            return render(request,"mobile/errorpage.html")
        else:
            return func(request)
    return inner
def admin_permission(func):
    def inner(request,id):
        if not request.user.is_superuser:
            return render(request,"mobile/errorpage.html")
        else:
            return func(request,id)
    return inner
def user_permission_requied(func):
    def inner(request):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return func(request)
    return inner
def user_permission(func):
    def inner(request,id):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return func(request,id)
    return inner


def view_cart(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobile/listmobiles.html",context)


@admin_permission_requied
def brand_view(request):
    form=BrandcreateForm()
    brands = Brands.objects.all()
    context = {}
    context["form"] = form
    context["brands"] = brands
    if request.method=="POST":
        form=BrandcreateForm(request.POST)
        if form.is_valid():
            form.save()
            print("brand saved")
            return render(request,"mobile/brandcreate.html",context)

    return render(request,"mobile/brandcreate.html",context)
@admin_permission
def brand_edit(request,id):
    brand=Brands.objects.get(id=id)
    form=BrandcreateForm(instance=brand)
    brands = Brands.objects.all()
    context={}
    context["form"]=form
    context["brands"] = brands
    if request.method=='POST':
        form=BrandcreateForm(request.POST,instance=brand)
        if form.is_valid():
            form.save()
            return redirect("bnd")
    else:
        return render(request,"mobile/brandedit.html",context)


@admin_permission
def brand_delete(request,id):
    brand=Brands.objects.get(id=id)
    brand.delete()
    return redirect("bnd")


@user_permission_requied
def mobile_view(request):
    form = MobilecreateForm()
    mobiles = Mobile.objects.all()
    context = {}
    context["form"] = form
    context["mobiles"] = mobiles
    if request.method == "POST":
        form = MobilecreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("mobile saved")
            return render(request, "mobile/mobileadd.html", context)
        return redirect("list")

    return render(request, "mobile/mobileadd.html", context)


def mob_details(request,id):
    mobile = Mobile.objects.get(id=id)
    context = {}
    context["mobile"] = mobile
    return render(request, "mobile/mobdetail.html", context)

@user_permission
def mobile_edit(request,id):
    mobile=Mobile.objects.get(id=id)
    form=MobilecreateForm(instance=mobile)
    mobiles = Brands.objects.all()
    context={}
    context["form"]=form
    context["mobiles"] = mobiles
    if request.method=='POST':
        form=MobilecreateForm(request.POST,instance=mobile)
        if form.is_valid():
            form.save()
            return redirect("mob")
    else:
        return render(request,"mobile/mobileedit.html",context)


@user_permission
def mobile_delete(request,id):
    mobile=Mobile.objects.get(id=id)
    mobile.delete()
    return redirect("mob")

def user_register(request):
    form=UserRegisterForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print("registered")
            return render(request,"mobile/loginuser.html",context)
        return render(request,"mobile/registeruser.html",context)
    return render(request, "mobile/registeruser.html", context)

def user_login(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pwd")
        user=authenticate(request, username=username,password=password)
        if user:
            login(request,user)
            print("login success")
            return redirect("list")
        else:
            print("login failed")
            return render(request,"mobile/loginuser.html")

    return render(request, "mobile/loginuser.html")

def user_logout(request):
    logout(request)
    return redirect("list")

@user_permission_requied
def feedback(request):
    if request.method == "POST":
        feedback = request.POST.get("fd")
        print(feedback)
        return redirect("list")
    return render(request,"mobile/feedback.html")


@user_permission
def purchase(request,id):
   items=Mobile.objects.get(id=id)
   username=request.user
   form=UserpurchaseForm(initial={'user':username,'items':items})
   context={}
   context["form"]=form
   context["items"] = items
   if request.method=='POST':
      form=UserpurchaseForm(request.POST)
      print("testpoint")
      if form.is_valid():
          print("testpoint get")
          form.save()
          return redirect("cart")
      else:
          context["form"]=form
          return render(request,"mobile/purchase.html",context)
   return render(request, "mobile/purchase.html", context)

def cart(request):
    orders=Myorders.objects.all()
    mobiles=Mobile.objects.all()
    context = {}
    context["orders"] = orders
    context["mobiles"] = mobiles
    total=0
    for order in orders:
        total+=order.items.price
    print(total)
    context["total"] = total
    return render(request,"mobile/mycart.html",context)

def errorpage(request):
    return render(request,"mobile/errorpage.html")


def item_delete(request,id):
    order=Myorders.objects.get(id=id)
    order.delete()
    return redirect("cart")




