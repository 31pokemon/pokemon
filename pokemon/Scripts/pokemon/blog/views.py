from django.shortcuts import render,redirect,get_object_or_404
from .models import Monster,Type
from .form import PostForm
from django.core.urlresolvers import reverse
# Create your views here.
def post_list(request):
    Monsters=Monster.objects.filter(name__isnull=False)
    return render(request, 'blog/post_list.html', {'Monsters':Monsters})#前面的Type是鍵，後面的type是值

def post_new(request):
    if request.method == "POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author = request.user
            post.publish()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html',{'form':form})

def post_detail(request,pk):
    monster=Monster.objects.get(pk=pk)
    return render(request,'blog/post_detail.html',{'monster':monster})

def post_edit(request,pk):
    monster=get_object_or_404(Monster,pk=pk)
    if request.method=="POST":
        form=PostForm(request.POST, instance=monster)
        if form.is_valid():
            post=form.save(commit=False)
            post.publish()
            post.save()
            return redirect('post_detail', pk=monster.pk)
    else:
        form = PostForm(instance=monster)
    return render(request, 'blog/post_edit.html',{'form': form})

def post_delete(request,pk):
    monster=Monster.objects.get(pk=pk)
    monster.delete()
    return render(request,'blog/post_list.html',{})
    
