from turtle import title
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication

def create(request):
    art1 = Article(headline="Artículo primero")
    art1.save()
    art2 = Article(headline="Artículo segundo")
    art2.save()
    art3 = Article(headline="Artículo tercero")
    art3.save()


    pub1 = Publication(title="Publicación primera")
    pub1.save()
    pub2 = Publication(title="Publicación segunda")
    pub2.save()
    pub3 = Publication(title="Publicación tercera")
    pub3.save()
    pub4 = Publication(title="Publicacion cuarta")
    pub4.save()
    pub5 = Publication(title="Publicación quinta")
    pub5.save()
    pub6 = Publication(title="Publicacion sexta")
    pub6.save()
    pub7 = Publication(title="Publicacion séptima")
    pub7.save()

    art1.publications.add(pub1)
    art1.publications.add(pub2)
    art1.publications.add(pub3)
    art2.publications.add(pub4)
    art2.publications.add(pub5)
    art3.publications.add(pub6)
    art3.publications.add(pub7)


    # art1.publications.remove(pub1)
   # pub1 = Publication.objects.get(id=1)
    result = pub1.article_set.all()

    return HttpResponse(result)