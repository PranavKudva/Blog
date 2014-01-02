from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from core.models import Blog


class SearchResults(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

def post(request):
    Blog.objects.create(
        title=request.POST['title'],
        content=request.POST['contents']
    )

    return HttpResponse('Lekhana has been posted')


def search(request):
    title = request.GET['title']
    foundblogs = Blog.objects.all().filter(title__icontains=title)

    return render(request, 'searchBlog.html', {
        'foundblogs': foundblogs,
        'title': title
    })


def view(request):
    blog = Blog.objects.get(title=request.GET['title'])

    return render(request, 'viewBlog.html', {
        'blog': blog
    })

def delete(request):
    Blog.objects.all().filter(title=request.GET['title']).delete()

    return render(request, 'writeBlog.html')