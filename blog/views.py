from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import Http404

from .forms import *
from .models import *


def blog_home_view(request):
    post = Post.objects.filter(status='pub').order_by('-date_created')[:6]
    print(request.GET.get('localhost'))
    context = {
        'post': post
    }
    return render(request, 'blog/HomeView.html', context)


def blog_list_view(request):
    post = Post.objects.filter(status='pub')
    # paginator
    paginator = Paginator(post, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/BlogList.html', context)


def blog_detail_view(request, pk):
    form = CommentForm()
    try:
        post = get_object_or_404(Post, pk=pk)
        comments = Comment.objects.filter(post=post).order_by('-date_created')
        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }
    except Http404:
        return render(request, '404.html')
    return render(request, 'blog/BlogDetail.html', context)


def blog_comment_create_view(request, pk):
    try:
        if request.user.is_authenticated:
            form = CommentForm(request.POST or None)
            post = get_object_or_404(Post, id=pk)
            comments = Comment.objects.filter(post=post).order_by('-date_created')
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                instance.post.add(post)
                return redirect('blog_detail', pk)
            context = {
                'form': form,
                'post': post,
                'comments': comments,
            }
        else:
            return redirect('home_view')
    except Http404:
        return render(request, '404.html')
    return render(request, 'blog/BlogDetail.html', context)


def blog_updateComment_view(request, pk):
    try:
        comment = get_object_or_404(Comment, id=pk)
        post = comment.post.get(comment=comment)
        comments = Comment.objects.filter(post=post).order_by('-date_created')
        form = CommentForm()
        updateComment = UpdateCommentForm(request.POST or None, instance=comment)
        if updateComment.is_valid():
            updateComment.save()
            return redirect('blog_detail', post.id)
        context = {
            'updateComment': updateComment,
            'form': form,
            'post': post,
            'comments': comments,
            'pk': pk,
        }
        return render(request, 'blog/BlogDetail.html', context)
    except Http404:
        return render(request, '404.html')


def blog_deleteComment_view(request, pk, pk_post):
    get_object_or_404(Comment, id=pk).delete()
    return redirect('blog_detail', pk_post)
