from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, RegisterForm
from . models import RegistrationModel


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is None:
            messages.info(request, 'Invalid credentials')
        else:
            auth.login(request, user)  # Log in
            return redirect('new_page')  # Redirect to the homepage

    return render(request, 'login.html')


def new(req):
    return render(req, 'new_page.html')


def form(req):
    if req.method == 'POST':

        return redirect('success_page')
    return render(req, 'form.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
    else:
        form = RegistrationForm()

    return render(request, 'register2.html', {'form': form})



def depend(req):
    return render(req, 'form2.html')

def success_page(req):
    return render(req, 'success.html')


def engineer(req):
    return redirect('https://en.wikipedia.org/wiki/Engineering')


def medical(req):
    return redirect('https://en.wikipedia.org/wiki/medic')


def law(req):
    return redirect('https://en.wikipedia.org/wiki/law')



def commerce(req):
    return redirect('https://en.wikipedia.org/wiki/commerce')


def hospitality(req):
    return redirect('https://en.wikipedia.org/wiki/hospitality')


# def form(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             # Form data is valid, process it here
#             # Access the form fields using cleaned_data dictionary
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             dob = form.cleaned_data['dob']
#             gender = form.cleaned_data['gender']
#             age = form.cleaned_data['age']
#             number = form.cleaned_data['number']
#             address = form.cleaned_data['address']
#             department = form.cleaned_data['department']
#             courses = form.cleaned_data['courses']
#             purpose = form.cleaned_data['purpose']
#             materials_provided = form.cleaned_data['materials_provided']
#
#             registration = RegistrationModel(name=name, email=email, dob=dob, gender=gender, age=age,
#                                              number=number, address=address, department=department,
#                                              courses=courses, purpose=purpose, materials_provided=materials_provided)
#             registration.save()
#             # For now, we'll just redirect to a success page
#             return redirect('success_page')
#     else:
#         form = RegisterForm()
#
#     return render(request, 'form.html', {'form': form})
