from django.shortcuts import render, redirect
from matplotlib.pyplot import text, title



from .models import BlogPost
from .forms import BlogForm

# Create your views here.

def index(request):
    """home page Blog"""
    blogs = BlogPost.objects.order_by('-date_added')   
    context = {'blogs': blogs, 'text': text}
    return render(request, 'blogs_first/index.html', context)

def new_topic(request):
    """define new topic"""
    if request.method != 'POST':
        # date did not send; create new form
        form = BlogForm()
    else:
        # date is sent; process date
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs_first:index')
    # display empty or wrong form
    context = {'form': form}
    return render(request, 'blogs_first/new_topic.html', context)

def edit_blog(request, blog_id):
    """edit exists topic"""
    blog = BlogPost.objects.get(id=blog_id)
    
    title = blog.title
    text = blog.text

    if request.method != 'POST':
        form = BlogForm(instance=blog)
    else:
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs_first:index')

    context = {'topic': blog, 'blog_id': blog.id, 'title': title, 'text': text, 'form': form}
    return render(request, 'blogs_first/edit_blog.html', context)        

