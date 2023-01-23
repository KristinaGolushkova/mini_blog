from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Rubric, Ad, Likes
from .form import CommentsForm


class PostViews(View):
    '''вывод записей'''

    def get(self, request):
        posts = Ad.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})


class PostDetail(View):
    '''отдельная страница записи'''

    def get(self, request, pk):
        post = Ad.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'ad': post})


class AddComments(View):
    '''Добавление комментария'''

    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


def get_client_ip(request):
    x_forward = request.META.get('HTTP_X_FORWARD')
    if x_forward:
        ip = x_forward.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')


class Dellike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')
