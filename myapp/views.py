# myapp/views.py
from django.shortcuts import render
from .forms import PostForm

def post_new(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

    else :
        form = PostForm()        

    return render(request, 'myapp/post_form.html', {
        'form' : form,
    })