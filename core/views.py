from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from core.models import Blog


class SearchResults(forms.Form):
    title = forms.CharField()
    content = forms.CharField()


def post(request):
    Blog.objects.create(
        title=request.POST['title'],
        content=request.POST['contents']
    )

    blog = Blog.objects.get(title=request.POST['title'])

    return redirect('/home/view/?id=' + str(blog.id))


def search(request):
    title = request.GET['title']
    foundblogs = Blog.objects.all().filter(title__icontains=title)

    return render(request, 'searchBlog.html', {
        'foundblogs': foundblogs,
        'title': title
    })


def manip(request):
    if request.POST['action'] == 'Delete':
        return delete(request.POST['id'])

    else:
        blog = Blog.objects.get(pk=request.POST['id'])
        return render(request, 'editBlog.html', {'blog': blog})


def delete(id):
    Blog.objects.all().filter(pk=id).delete()

    return redirect('/home/')


def view(request):
    blog = Blog.objects.get(pk=request.GET['id'])

    return render(request, 'viewBlog.html', {
        'blog': blog
    })


def update(request):
    Blog.objects.filter(pk=request.POST['id']).update(title=request.POST['newTitle'],
                                                      content=request.POST['newContent'])

    return redirect('/home/view/?id=' + request.POST['id'])