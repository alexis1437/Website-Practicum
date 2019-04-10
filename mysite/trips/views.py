from django.views.generic import ListView
from django.shortcuts import render
from .models import Post, Visit
from django.http import HttpResponseRedirect

def listpost(request):
    if request.method == 'POST':
        if request.POST.get('content'):
            post=Post()
            if request.POST.get('name'):
                post.user= request.POST.get('name')
            else:
                post.user="Anonymous"
            post.text= request.POST.get('content')
            post.uid = request.COOKIES.get('uid')
            post.save()
    posts = Post.objects.all()
    visits = 1
    if request.COOKIES.get('visits'):
        visits = int(request.COOKIES.get('visits')) + 1
        uid = request.COOKIES.get('uid')
    else:
        _n = Visit.objects.get(pk=1)
        _n.passenger+=1
        uid = str(_n.passenger)
        _n.save()
    _n = Visit.objects.get(pk=1)
    response = render(request,'home.html',{
        'posts': posts,
        'visits': visits,
        'passenger': _n.passenger,
        'uid': uid,
    })
    response.set_cookie('visits', str(visits),  3600 * 24 * 365 * 2)
    response.set_cookie('uid', str(uid), 3600 * 24 * 365 * 2)
    return response


def delete(request, post_id=None):
    uid = request.COOKIES.get('uid')
    post = Post.objects.get(id=post_id)
    if uid == post.uid:
        post.delete()
    return HttpResponseRedirect('/')
