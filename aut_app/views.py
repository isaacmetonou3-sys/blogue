from django.shortcuts import render, get_object_or_404, redirect

from .models import Article

def Accueil(request):
    article = Article.objects.all()

    context = {
        "article": article,
    }

    return render(request, "base.html", context)


def lire(request, id):
    article = get_object_or_404(Article, id=id)

    autres_articles = Article.objects.exclude(id=id)

    return render(request, "lire.html", {
        "article": article,
        "autres_articles": autres_articles,
    })



