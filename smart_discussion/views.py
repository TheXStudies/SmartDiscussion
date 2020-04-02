from django.shortcuts import render, redirect
from django.views.generic import CreateView

from smart_discussion.models import Article


def index(request):
    ctx = {
        'articles': Article.objects.all(),
    }
    return render(request, 'index.html', ctx)


def logout(request, next_page='index'):

    return redirect(next_page)


class ArticleCreate(CreateView):
    template_name = "new_article.html"
    model = Article
    fields = ['title', 'text']