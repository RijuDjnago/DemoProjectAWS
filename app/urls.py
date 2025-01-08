from django.urls import path
from .views import *

urlpatterns = [
    path('', base, name="base"),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
]