from django.shortcuts import render,HttpResponse,redirect
from .models import quiz
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import quizForm



# Create your views here.
def home(request):
              quizs = quiz.objects.all().order_by('-posted_at')
              return render(request,"home.html",{'quizs':quizs})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



def create(request):
    if request.method == 'POST':
        form = quizForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()  
            return redirect('home')  
    else:
        form = quizForm()

    return render(request, 'create.html', {'form': form})

