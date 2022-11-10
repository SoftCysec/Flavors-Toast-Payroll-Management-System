from django.shortcuts import render,redirect
from .models import Employee, Jobs, Deductions
from .forms import EmployeesForm, JobsForm, DeductionsForm
from django.contrib.auth import logout 
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "POST":
        user = request.POST['login']
        password = request.POST['password']

        if user == "admin" and password == "password":
            return redirect("home")

    return render(request,'login.html')

def home(request):
    countJobs = Jobs.objects.all().count()
    countEmp = Employee.objects.all().count()
    data = Employee.objects.all()
    context = {
        "countJobs" : int(countJobs),
        "countEmp" : int(countEmp),
        "data" : data,
    }

    return render(request,'home.html',context)

def createEmployee(request): 
    form = EmployeesForm(request.POST or None)

    if form.is_valid():
        
        form.save()
        form.cleaned_data['jobDesc'].save()
        
        return redirect('employee')   

    return render(request,'createEmployee.html',{'form':form})    

def employee(request):
    data = Employee.objects.all()
    context = {
        "data" : data,
    }
    return render(request,'employee.html',context)


def jobs(request):
    obj = Jobs.objects.all()
    context = {
        "data" : obj,
    }
    return render(request,'jobs.html',context)

def createJobs(request): 
    form = JobsForm(request.POST or None)
    if form.is_valid():
        
        form.save()

        
        return redirect('jobs')   

    return render(request,'createJobs.html',{'form':form}) 

def deductions(request):
    obj = Deductions.objects.all()
    total = 0
    for i in obj:
        total += float(i.deduct)

    context = {
        "data" : obj,
        "total" : total,
    }
    
    return render(request,'deductions.html',context)

def createDeductions(request): 
    form = DeductionsForm(request.POST or None)
    if form.is_valid():
        
        form.save()

        
        return redirect('deductions')   

    return render(request,'createDeductions.html',{'form':form}) 


def salaryReport(request): 
    
    emp = Employee.objects.all()

    deduction = Deductions.objects.all()
    totalDeduct = 0
    for i in deduction:
        totalDeduct += float(i.deduct)



    context={
        "data" : emp,
        "totalDeduction" : totalDeduct,
    }

    


    return render(request,'salaryReport.html',context) 

    
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("/")