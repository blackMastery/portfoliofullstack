from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,\
PageNotAnInteger

from django.views.generic import ListView
from django.db.models import Count


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 6
    template_name = 'blog/post/list.html'

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request,
    'blog/post/list.html',
    {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
    status='published',
    publish__year=year,
    publish__month=month,
    publish__day=day)

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)
    similar_posts =  similar_posts.annotate(same_tags=Count('tags'))\
        .order_by('-same_tags','-publish')[:4]

    return render(request,'blog/post/detail.html',{'post': post, 'similar_posts':similar_posts})