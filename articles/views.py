from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    object_list = Article.objects.order_by('-published_at')
    template = 'articles/news.html'
    context = {
        'object_list': object_list,
        'page_title': 'Новости на сайте'
    }

    ordering = '-published_at'

    return render(request, template, context)
