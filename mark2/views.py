from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import quiz
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import quizForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.

#home page
def home(request):
            quizs = quiz.objects.all().order_by('-posted_at')
            return render(request,"home.html",{'quizs':quizs})


# login page
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#     return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Logs in the user
            return redirect('home')  # Redirect to home page after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')  # Render the login form for GET requests





# register page
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('register')

        # Create the user and save it to the auth_user table
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "User registered successfully!")
        return redirect('login')

    return render(request, 'register.html')




# Quiz creation page
# @login_required(login_url='/login/')
# def create(request):
#     if request.method == 'POST':
#         form = quizForm(request.POST, request.FILES)  
#         if form.is_valid():
#             form.save()  
#             return redirect('home')  
#     else:
#         form = quizForm()
    
#     return render(request, 'create.html', {'form': form})


@login_required(login_url='/login/')  # Redirects unauthenticated users to the login page
def create(request):
    if request.method == 'POST':
        form = quizForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()  
            return redirect('home')  
    else:
        form = quizForm()
        pass
    return render(request, 'create.html',{'form': form})



@login_required(login_url='/login/')

def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('home.html')  # Redirect to the home page or login page

@login_required
def delete(request,pk):
    quiz= get_object_or_404(quiz, pk=pk)
    if request.method == "POST":
        quiz.delete()
        return redirect('quiz') 
    return render(request, 'delete.html', {'quiz': quiz})