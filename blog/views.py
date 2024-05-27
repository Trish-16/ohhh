from django.contrib.auth import get_user_model
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import AddPostForm, UpdatePostForm
from .models import Post, Category


# def categories_list(request):
#     categories = Category.objects.all() #модель.метод() - чтобы достать оттуда данные
#     return render(request, 'blog/index.html', {'categories_list': categories})


# def posts_list(request):    #view в качестве функции всегда принимает request(запрос)
#     category = request.GET.get('category') #все query параметры
#     posts = Post.objects.filter(category_id=category)  #category__slug запрос будет дольше - SELECT * FROM post as p INNER JOIN category as c ON p.category_id=c.slug
#     # #SELECT * FROM post WHERE category_id='sport' -
#     return render(request, 'blog/posts_list.html', {'posts': posts}) #после создания view, нужно это импортировать в urls

#
# def post_details(request, pk):
#     try:
#         post = Post.objects.get(id=pk)
#     except Post.DoesNotExist:
#         raise Http404
#     return render(request, 'blog/post_details.html', {'post': post})
#
#
# def add_post(request):
#     if request.POST:
#         post_form = AddPostForm(request.POST, request.FILES)
#         if post_form.is_valid():
#             # title = post_form.cleaned_data.get('title', 'some_title') когда наследуется от Form
#             # category = post_form.cleaned_data.get('category')
#             # text = post_form.cleaned_data.get('text')
#             # User = get_user_model()
#             # user = User.objects.first()
#             # image = post_form.cleaned_data.get('image')
#             # post = Post.objects.create(title=title, category=category, text=text, user=user, image=image) #создать объект от модели
#             # return redirect(post.get_absolute_url())
#             post = post_form.save() #когда наследуется от ModelForm
#             return redirect(post.get_absolute_url())
#     else:
#         post_form = AddPostForm()
#     return render(request, 'blog/add_post.html', {'post_form': post_form})
#
#
# def update_post(request, pk): #pk чтобы определить, какой именно пост удалять по primary key
#     post = get_object_or_404(Post, pk=pk)
#     post_form = UpdatePostForm(request.POST or None, request.FILES or None,
#                                instance=post)
#     if post_form.is_valid():
#         post_form.save()
#         return redirect(post.get_absolute_url())
#     return render(request, 'blog/update_post.html', {'post_form': post_form, 'post': post})
#
#
# def delete_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('home-page')
#     return render(request, 'blog/delete_post.html', {})
