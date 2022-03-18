from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html', {'form': UserCreationForm})
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))
        else:
            username = form.data['username']
            password1 = form.data['password1']
            password2 = form.data['password2']
            for msg in form.errors.as_data():
                if msg == 'username':
                    messages.error(request, f'Username "{username}" is not valid')
                if msg == 'password2' and password1 == password2:
                    messages.error(request, "Password is not strong enough")
                elif msg == 'password2' and password1 != password2:
                    messages.error(request, "Passwords do not match")

    form = UserCreationForm
    return render(request, 'users/register.html', {"form": form})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]