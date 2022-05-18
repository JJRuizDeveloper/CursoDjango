from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Entry
from django.http import HttpResponse

def update(request):
    author = Author.objects.get(id=1)
    author.name = "Juanjo"
    author.email = "juanjo@demo.com"
    author.save()
    return HttpResponse("Modificado")

def queries(request):
    # Obtener todos los elementos
    authors = Author.objects.all()

    # Obtener datos filtrados por condición
    # filtered = Author.objects.filter(email='larry17@example.net')

    # Obtener un único objeto (filtrado)
    author = Author.objects.get(id=1)

    # Obtener los 10 primeros elementos
    limits = Author.objects.all()[:10]

    # Obtener 5 elementos saltando los 5 primeros
    offsets = Author.objects.all()[5:10]

    # Obtener todos los elementos ordenados
    orders = Author.objects.all().order_by('email')

    # Obtener todos los elementos cuyo id sea menor o igual a 15
    # filtered = Author.objects.filter(id__lte=15)

    # Obtener totos los autores que contienen en su nombre la palabta yes
    filtered = Author.objects.filter(name__contains="yes")

    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limits': limits, 'offsets': offsets, 'orders': orders})
