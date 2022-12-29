from django.urls import path
# Import views from current base app folder
from . import views

# Create base app urls
urlpatterns = [
    # Route for login page
    path('login/', views.loginPage, name="login"),
    # Route for login page
    path('logout/', views.logoutUser, name="logout"),
    # Route for register page
    path('register/', views.registerUser, name="register"),
    # Add path to route to yogas page view function
    path('', views.yogas, name="yogas"),
    # Add path to route to yoga page view function
    # Use id passed in url to get yoga
    path('yoga/<str:pk>/', views.yoga, name="yoga"),
    # Route to add yoga using form
    path('add_yoga/', views.addYoga, name="add_yoga"),
    # Route to edit yoga using form
    path('update_yoga/<str:pk>/', views.updateYoga, name="update_yoga"),
    # Route to delete yoga
    path('delete_yoga/<str:pk>/', views.deleteYoga, name="delete_yoga"),
]