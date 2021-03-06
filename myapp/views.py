# myapp/views.py
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def post_new(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            post.save()
            return redirect('/')

    else :
        form = PostForm()        

    return render(request, 'myapp/post_form.html', {
        'form' : form,
    })