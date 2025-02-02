from django.shortcuts import render,redirect
from django.http import HttpResponse
from managsys.models import *
from datetime import *
# Create your views here.

def home(request):
    return render(request,"main.html")

def book(request):
    b = books.objects.all()
    return render(request,"manage_books.html",{'b':b})

def stu(request):
    s = student.objects.all()
    return render(request,"student.html",{'s':s})

def issuing(request):
    i = issue.objects.all()
    return render(request,"issue_table.html",{'iss':i})

def manage(request):
    return redirect('../manage1')

def students(request):
    return redirect('../stu')

def issues(request):
    return redirect('../issuing')

def ins(request):
    u=books()
    u.bookid=request.GET['id']
    u.bname=request.GET['book']
    u.author=request.GET['author']
    u.quantity=request.GET['quantity']
    u.save()
    return redirect('../manage1')

def stuins(request):
    u=student()
    u.s_id=request.GET['card']
    u.sname=request.GET['stu']
    u.phone=request.GET['phone']
    u.email=request.GET['email']
    u.save()
    return redirect('../student')

def issert(request):
    u=issue()
    x=request.GET['sid']
    y=request.GET['bid']
    z = books.objects.get(bookid=y)
    if student.objects.filter(s_id=x) and books.objects.filter(bookid=y) and (z.quantity != 0) :
        u.s_id=x
        u.b_id=y
        u.i_date=request.GET['isd']
        z.quantity = z.quantity - 1
        u.save()
        z.save()
        return redirect('../issuing')
    else:
        return redirect('../issuing')

def edit(request,id):
    e=issue.objects.get(id=id)
    return render(request,'edit.html',{'e':e})

def edcode(request,id):
    e = issue.objects.get(id=id)
    z = books.objects.get(bookid=e.b_id)
    e.r_date = datetime.date(datetime.strptime(request.GET['rtd'], '%Y-%m-%d'))
    e.save()
    d=e.r_date - e.i_date
    e.fine=d.days*5
    e.save()
    z.quantity = z.quantity + 1
    z.save()
    
    return redirect('../issuing')

def delis(request,id):
    d = issue.objects.get(id=id)
    d.delete()
    return redirect('../issuing')

def delib(request,id):
    d = books.objects.get(id=id)
    d.delete()
    return redirect('../manage1')

def delis(request,id):
    d = student.objects.get(id=id)
    d.delete()
    return redirect('../stu')

def logon(request):
    a = request.GET['username']
    b = request.GET['password']

    if login.objects.filter(a_id=a,pwd=b):
        return render(request,'main.html')
    else:
        return render(request,'index.html')
    
def log(request):
    return render(request,'index.html')

