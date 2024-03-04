from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
import string 
import random 
def generate_password():
    password_length = 8
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(password_length))
    return password



