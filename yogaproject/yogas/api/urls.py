# Import path
from django.urls import path
# Import api views
from . import views

# Define API routes
urlpatterns = [
    path('',  views.getRoutes),
    path('yogas/', views.getYogas),
    path('yogas/<str:pk>/', views.getYoga),
]
