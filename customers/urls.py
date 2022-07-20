from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('client/<int:id>/update/',update, name="update"),
    path('client/<int:id>/delete/',delete, name="delete")

]