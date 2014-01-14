from django.shortcuts import render, redirect
from core.models import Blog, User


def post(request):
    Blog.objects.create(
        title=request.POST['title'],
        content=request.POST['contents']
    )

    blog = Blog.objects.get(title=request.POST['title'])

    return redirect('/home/view/?id=' + str(blog.id))


def search(request):
    print(type(request))

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


def create(username, password):
    return User.objects.get_or_create(user_name=username, password=password)


def create_user(request):
    username = request.POST['Username']
    password = request.POST['Password']
    password_again = request.POST['PasswordAgain']

    if password_again == password:
        user, user_created = create(username, password)
        if not user_created:
            message = "Username %s already exists! Please try other names." % username
            return render(request, "signup.html", {'message': message})
        return redirect("/login/")

    return render(request, "signup.html", {'message': "Passwords did not match! Please retry again."})


def authenticate(request):
    return redirect('/home/')


def signup(request):
    return render(request, "signup.html")