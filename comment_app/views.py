from django.shortcuts import render, get_object_or_404 , redirect
from .models import Post, Category


from .forms import CommentForm
# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def list_of_post_by_category(request,category_slug):
	categories  = Category.objects.all()
	post = Post.objects.filter(status = 'published')
	if category_slug:
		category = get_object_or_404(Category , slug = category_slug)
		post = post.filter(category = category)
	template = 'comment_app/category/list_of_post_by_category.html'
	context = {'categories': categories, 'post':post,'category':category}
	return render(request,template,context)


@login_required(login_url="/login/")
def list_of_post(request):
	post = Post.objects.filter(status = 'published')
	template = 'comment_app/post/list_of_post.html'
	context = {'post':post}
	return render(request,template,context)
@login_required(login_url="/login/")
def post_detail(request,slug):
	post = get_object_or_404(Post,slug = slug)
	template = 'comment_app/post/post_detail.html'
	context = {'post':post}
	return render(request,template, context)
#--------------------------------------------------------------------------------------------------
@login_required(login_url="/login/")
def add_comment(request,slug):
	post = get_object_or_404(Post,slug = slug)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.post = post
			comment.save()
			return redirect('comment_app:post_detail',slug = post.slug)
	else:
		form = CommentForm()
	template = 'comment_app/post/add_comment.html'
	context = {'form':form}
	return render(request,template, context)