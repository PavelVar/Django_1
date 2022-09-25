from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date')[0:]
    data = {'page_name': 'News page',
            'title': 'News',
            'news': news
            }
    return render(request, 'news/news_home.html', data)


def create_article(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else: error = 'Error message'

    form = ArticleForm()
    data = {'page_name': 'Create article page',
            'title': 'Create',
            'form': form,
            'error': error,
            }
    return render(request, 'news/create.html', data)


def contacts(request):
    return render(request, 'main/contacts.html')


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail-view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticleForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-del.html'

