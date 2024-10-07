# library/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Book  # Import Book model


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after successful login
        else:
            return render(request, 'library/login.html', {'error': 'Invalid username or password'})
    return render(request, 'library/login.html')

def book_category(request):
    categories = Book.objects.values('category').distinct()  # Assuming you have a category field in your Book model
    return render(request, 'library/book_category.html', {'categories': categories})