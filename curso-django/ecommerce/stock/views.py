from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProductForm

def index(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'form': form})
    else:    
        form = ProductForm()
        return render(request, 'index.html', {'form': form})