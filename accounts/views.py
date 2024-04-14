from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm, User
from blog.forms import *


def accounts_profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    postForm = PostForm()
    posts = Post.objects.filter(author=request.user).order_by('-date_created')
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'postForm': postForm,
        'page_obj': page_obj,
    }
    return render(request, 'registration/profile.html', context)


def accounts_register_view(request):
    registerForm = UserCreationForm(request.POST or None)
    if registerForm.is_valid():
        registerForm.save()
        return redirect('login')
    context = {
        'registerForm': registerForm
    }
    return render(request, 'registration/register.html', context)


def accounts_addPost_view(request):
    postForm = PostForm(request.POST or None)
    if postForm.is_valid():
        instance = postForm.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('blog_detail', instance.pk)
    context = {
        'postForm': postForm,
    }
    return render(request, 'registration/profile.html', context)


def accounts_deletePost_view(request, pk):
    try:
        get_object_or_404(Post, id=pk).delete()
        return redirect('profile_view')
    except Http404:
        return render(request, '404.html')


def accounts_updatePost_view(request, pk):
    try:
        post = get_object_or_404(Post, id=pk)
        updateForm = PostForm(request.POST or None, instance=post)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('profile_view')
        context = {
            'updateForm': updateForm,
            'postForm': PostForm(),
            'pk': pk,
        }
        return render(request, 'registration/profile.html', context)

    except Http404:
        return render(request, '404.html')
