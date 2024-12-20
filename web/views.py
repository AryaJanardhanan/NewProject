from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")

@login_required
def about(request):
    return render(request, "about.html")

def base(request):
    return render(request, "base.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            ms = form.cleaned_data['msg']
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form':form})

def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = StudentForm()
    return render(request, "student.html", {'form':form})

def sample(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('eml')
        place = request.POST.get('msg')
        st = Student.objects.create(name=name, phone=phone, place=place)
        st.save()
        return redirect('home')
    else:
        return render(request, "message.html")


def register(request):
    if request.method == 'POST':
        form = UserregForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data.get('password1')
            user.set_password(raw_password)
            user.save()

            fn = form.cleaned_data.get('first_name')
            ln = form.cleaned_data.get('last_name')
            un = form.cleaned_data.get('username')
            pro = profile.objects.create(user=user,f_name=fn, l_name=ln, username=un )
            return redirect('uslogin')
    else:
        form = UserregForm()
    return render(request, "register.html", {'form':form})

def uslogin(request):
    if request.method == 'POST':
        form = UserloginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserloginForm()
    return render(request, "userlogin.html", {'form':form})


def logt(request):
    logout(request)
    return redirect('base')


def disply(request):
    stu = Student.objects.all()
    return render(request, "display.html", {'items':stu})

def delt(request, pk):
    item = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('display')
    
def editt(request, pk):
    item = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = StudentForm(instance=item)
    return render(request, "editstudent.html", {'form':form})
