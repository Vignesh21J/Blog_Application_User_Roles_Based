from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Published', category=category_id)

    # category = Category.objects.get(pk=category_id)
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)


def blogs(request, blog_slug):
    single_blog = get_object_or_404(Blog, slug=blog_slug, status='Published')
    
    context = {
        'single_blog':single_blog
    }
    return render(request, 'blogs.html', context)