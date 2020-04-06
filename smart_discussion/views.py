from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic.edit import ModelFormMixin
from django.forms.widgets import HiddenInput

from smart_discussion.models import Article


def index(request):
    ctx = {
        'articles': Article.objects.all(),
    }
    return render(request, 'index.html', ctx)


def logout(request, next_page='index'):

    return redirect(next_page)


class ArticleCreate(CreateView):
    class Meta:
        widgets = {
            'author': HiddenInput(),
        }

    success_url = "/"
    template_name = "new_article.html"
    model = Article
    fields = ['title', 'text']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        # if not form_kwargs['instance']:
        #     form_kwargs.setdefault('initial', {})['author'] = self.request.user
        # else:
        #     form_kwargs.setdefault('data', {})['author'] = self.request.user
        #
        return form_kwargs
