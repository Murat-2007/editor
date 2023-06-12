from django.http.response import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib import messages


from .models import Post
from .forms import Personal_infoForm,PostForm

#messages = []
def index(request):
    selam = "Konnichiva Nihon"
    return HttpResponse(selam)

def personal_info(request):
    form = Personal_infoForm(data=request.GET or None) 
    
    if form.is_valid():
        name = form.cleaned_data.get('name')
        surname = form.cleaned_data.get('surname')
        email = form.cleaned_data.get('email')
        content = form.cleaned_data.get('content')
        data = {'name': name, 'surname': surname, 'email': email, 'content': content}
        messages.append(data)

        return render(request, 'personal_info.html', context={'messages': messages, 'form': form})
    return render(request, 'personal_info.html', context={'form': form})

def article_list(request):
    post = Post.objects.all()
    
    context = {'posts': post}
    return render(request, 'posts/article_list.html', context)

def article_create(request):
    print(request.FILES)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(data=request.POST, files=request.FILES or None)
        if form.is_valid():
            post = form.save()
            msg = "Congratulations, <strong> %s</strong> your article has been created successfully" %(post.title)
            messages.success(request,msg,extra_tags='success')
            #reverse('article_detail', kwargs={'pk':post.pk})
            return HttpResponseRedirect(post.get_absolute_url())
    return render(request, 'posts/article_create.html', context={'form': form})

def article_detail(request,slug):
    post = get_object_or_404(Post, slug=slug)
    
    return render(request, 'posts/article_detail.html', context={'post': post})

def article_update(request,slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(instance=post, data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save()
        msg = "Congratulations, <strong> %s</strong> your article has been updated successfully" %(post.title)
        messages.success(request,msg,extra_tags='info')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {'form': form, 'post': post}
    return render(request, 'posts/article_update.html', context=context)

def article_delete(request,slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    msg = "<strong> %s</strong> your article has been deleted successfully" %(post.title)
    messages.success(request,msg,extra_tags='danger')
    return HttpResponseRedirect(reverse(article_list))


def accept(request):
    accepted = "accepted articles"
    return HttpResponse(accepted)

def revize(request):
    revized = "revized articles"
    return HttpResponse(revized)

def reject(request):
    rejected = "rejected articles"
    return HttpResponse(rejected)


