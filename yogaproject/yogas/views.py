from atexit import register
from django.shortcuts import render
# Import HTTP
from django.http import HttpResponse, HttpResponseRedirect
# Import redirect
from django.shortcuts import redirect
from django.urls import reverse

from .forms import YogaForm

# Import yoga model from models
from .models import Yoga

# Import User Model
from django.contrib.auth.models import User
# Import authenticate, login and logout functions
from django.contrib.auth import authenticate, login, logout
# Import decorator to check login for view
from django.contrib.auth.decorators import login_required
# Import UserCreationForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# View to handle user login


def loginPage(request):
    # Used in login_or_register to determine page
    page = 'login'
    # Check is user is logged in
    if request.user.is_authenticated:
        # Redirect to home if logged in
        return redirect('/')

    # Submitted login form
    if request.method == 'POST':
        # Get email and password
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        # Try to get user by username
        try:
            user = User.objects.get(username=username)
        except:
            print('User does not exist')

        # Verify password entered matches user password hash
        user = authenticate(request, username=username, password=password)

        # If user was returned
        if user is not None:
            # Login and set cookie
            login(request, user)
            return redirect('/')
        else:
            print('Invalid username or passwors')

    # Render login_register page
    context = {'page': page}
    return render(request, 'login_register.html', context)

# Function to logout user


def logoutUser(request):
    # Call user logout function to logout
    logout(request)
    return redirect('/')

# Function to register new user
def registerUser(request):
    # Get UserCreationForm from django
    form = UserCreationForm()

    if request.method == 'POST':
        # Pass form data to form
        form = UserCreationForm(request.POST)
        # If no errors in form
        if form.is_valid():
            # Build user object
            user = form.save(commit=False)
            user.username = user.username.lower()
            # Save new user in database
            user.save()
            # Login as new user
            login(request, user)
            # Redirect home
            return redirect('/')
        else:
            print("Error in registration")

    # Render register form
    return render(request, 'login_register.html', {'form': form})


# View for yogas
def yogas(request):
    # Get yogas from database using Queryset
    yogas = Yoga.objects.all()

    # Put page title and yogas array to be passed in context
    context = {
        "page_title": "Yoga Poses",
        "yogas": yogas,
    }

    # Render yogas template with context
    return render(request, "homepage.html", context)

# View for yoga based on id get param
def yoga(request, pk):
    # Use yoga manager(objects) to get yoga where id=pk
    yoga = Yoga.objects.get(id=pk)
    # Put page title and yoga to be passed in context
    context = {
        "page_title": "Yoga Pose",
        "yoga": yoga,
    }

    # Render yogas template with context
    return render(request, "yoga.html", context)

# Use decorator to check if user is logged
# in before they can add a yoga
@login_required(login_url="login")
def addYoga(request):
    form = YogaForm()
    # When form submitted

    '''
        form = YogaForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return HttpResponseRedirect(reverse('yogas'))
        else:
            context = {'form': form}
            return render(request, 'yoga_form.html', context)
    else:
        form = YogaForm()
        return render(request, 'yoga_form.html', {'form':form})
    '''
    if request.method == 'POST':
        # Create yoga object from form
        Yoga.objects.create(
            posted_by=request.user,
            name=request.POST.get('name'),
            level=request.POST.get('level'),
            image=request.FILES['image'],
            description=request.POST.get('description')            
        )
        # Redirect to homepage
        return redirect('/')

    context = {'form': form}
    return render(request, 'yoga_form.html', context)


@login_required(login_url="login")
# View to update yoga with form
def updateYoga(request, pk):
    # Get yoga object from db with id by using model
    yoga = Yoga.objects.get(id=pk)
    # Generate Yogaform for yoga
    form = YogaForm(instance=yoga)

    # User need to be logged in as well as
    # The user that posted the yoga
    if request.user != yoga.posted_by:
        return render(request, "not_authorized.html")

    # When form submitted get values
    if request.method == 'POST':
        # Update model based on form values
        yoga.name = request.POST.get('name')
        yoga.level = request.POST.get('level')
        yoga.image = request.FILES['image']
        yoga.description = request.POST.get('description')
        # Save model in db
        yoga.save()
        # Redirect to hom
        return redirect('/')

    # Return and render yoga form
    context = {'form': form, 'yoga': yoga}
    return render(request, 'yoga_form.html', context)

# Route to delete yoga


@login_required(login_url="login")
def deleteYoga(request, pk):
    # Get yoga object from db using model
    yoga = Yoga.objects.get(id=pk)

    # User need to be logged in as well as
    # The user that posted the yoga
    if request.user != yoga.posted_by:
        return render(request, "not_authorized.html")

    if request.method == 'POST':
        # Delete yoga object and dbs
        yoga.delete()
        # Returb home
        return redirect('/')
    # Render confirm delete page
    return render(request, 'delete.html', {'obj': yoga})
