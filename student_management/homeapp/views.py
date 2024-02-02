from django.shortcuts import render,redirect
from .models import Student
# from django.contrib import messages

# Create your views here.
def index_page(request):
    data = Student.objects.all()
    context = {'data':data}
    return render(request,"index.html",context)

def std_form(request):
    if request.method =='POST':
        first_name = request.POST.get('frt_name')
        last_name = request.POST.get('lst_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        s=Student()
        s.first_name = first_name
        s.last_name = last_name
        s.Phone_no = phone
        s.email=email
        s.save()
        return redirect(index_page)
    return render(request,"form.html",)
   
def delete_std(request,id):
    s = Student.objects.get(pk=id)
    s.delete()
    
    return redirect(index_page,)

def update_std(request,id):
    s=Student.objects.get(id=id)
    context = {'s':s}
    s.save()
    return render(request,"update.html",context)

def update_done(request,id):
    if request.method =='POST':
        first_name = request.POST.get('frt_name')
        last_name = request.POST.get('lst_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        s=Student.objects.get(pk=id)
        s.first_name = first_name
        s.last_name = last_name
        s.Phone_no = phone
        s.email=email
        s.save()
        
        return redirect(index_page)
    return render(request,"update.html")