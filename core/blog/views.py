from django.shortcuts import render
from django.views.generic.base import TemplateView
from blog.models import Post



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'mamzy'
        context['posts'] = Post.objects.all()
        return context
