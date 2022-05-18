from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

def create(request):
    rep = Reporter(first_name='Juanjo', last_name='Ruiz', email="juanjo@demo.com")
    rep.save()

    art1 = Article(headline='Lorem ipsum dolot', pub_date=date(2022,5,5), reporter=rep )
    art1.save()
    art2 = Article(headline='Lorem set aimet', pub_date=date(2022,3,7), reporter=rep )
    art2.save()
    art3 = Article(headline='dolot aimet lorem', pub_date=date(2022,4,9), reporter=rep )
    art3.save()
    
    result = rep.article_set.count()
   # result = rep.article_set.filter(headline='Lorem set aimet')
   # result = art1.reporter.first_name
   
    
    return HttpResponse(result)