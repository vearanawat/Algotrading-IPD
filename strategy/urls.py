from . import views
from django.urls import path


urlpatterns = [
    path('strategy/', views.strategy, name='strategy'),
]

