from django.urls import path
from . import views

urlpatterns = [
    # Add your other URL patterns here if needed
    
    # Define a URL pattern for the chatbot view
    path('', views.chatbot_view, name='chatbot_view'),
]
