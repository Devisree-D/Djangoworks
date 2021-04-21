from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
def get_cal(request):
    return render(request,"programone/calculation.html")
def cal_res(request):
    num1=int(request.POST.get("num1"))
    num2 =int(request.POST.get("num2"))
    add=num1+num2
    context={}
    context["rslt"]=add
    return render(request,"programone/calculation.html",context)

def check_prime(request):
    return render(request,"programone/check_prime.html")
def get_result(request):
    num=request.POST.get("num")
    num=int(num)
    flg=0
    if (num==1) :
        print(num,"is a prime number")
    elif (num==2):
        print(num,"is a prime number")
    else:
        for i in range(2,num):
            if(num%i==0):
                flg+=1
                break
            else:
                flg=0
        if flg==0:
            print(num,"is a prime number")
        else:
            print(num,"not a prime number")
    return render(request, "programone/check_prime.html")
def prime_list(request):
    return render(request,"programone/prime_list.html")
def get_list(request):
    low=request.POST.get("low")
    upp=request.POST.get("upp")
    low=int(low)
    upp=int(upp)
    flg = 0
    for num in range(low,(upp+1)):
        for i in range(2,num):
            if(num%i==0):
                flg+=1
                break
            else:
                flg=0
        if (flg==0) :
                print(num)
    return render(request,'programone/prime_list.html')

