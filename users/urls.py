from . import views
from django.urls import path


urlpatterns = [
    path('edit-profile/', views.editprofile, name='edit-profile'),
]

