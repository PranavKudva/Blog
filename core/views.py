from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from core.models import Blog


class SearchResults(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

# def write_blog(request):
#     if request.method == 'GET':
#         form = BlogCreater(request.POST)
#
#         if form.is_valid():
#             title = form.cleaned_data['title']
#
#             return HttpResponse('Posted Successfully')
#         else:
#             form = BlogCreater()
#
#         return render(request, 'writeBlog.html', {
#             'form': form
#         })

def post(request):
    Blog.objects.create(
        title=request.POST['title'],
        content=request.POST['contents']
    )

    return HttpResponse('Lekhana has been posted')


def search(request):
    foundblogs = Blog.objects.all().filter(title__icontains=request.GET['title'])
    if foundblogs.count() == 0:
          return render(request, 'noBlogFound.html')

    return render(request, 'searchBlog.html', {
        'foundblogs': foundblogs
    })


def view(request):
    blogs = Blog.objects.all().filter(title=request.GET['title'])

    return render(request, 'viewBlog.html', {
        'blogs': blogs
    })

def delete(request):
    Blog.objects.all().filter(title=request.GET['title']).delete()

    return render(request, 'writeBlog.html')

