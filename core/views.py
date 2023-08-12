from django.shortcuts import render,redirect,HttpResponse
from .models import Post,History,Like,Views,DisLike

# Create your views here.

def home(request,field=None):
    if request.method=='POST':
        pseudo_name=request.POST['pseudoname']
        title=request.POST['title']
        content=request.POST['content']
        field=request.POST['field']

        if len(pseudo_name)<3 or len(pseudo_name)>15:
            pass
        elif len(title)==0:
            pass
        elif len(content)==0:
            pass
        else:
            post=Post()
            post.pseudo_name=pseudo_name
            post.title=title
            post.content=content
            post.post_field=field
            post.save()
            history=History()
            history.session_key=request.session.session_key
            history.post=post
        
            history.save()
            print('Post Saved')

    posts=Post.objects.all()
    
    if not request.session.exists(request.session.session_key):
        request.session.create()
        print('Created')
    if field is None:
        if request.method=='GET':
            query=request.GET.get('query')
            if query is not None:
                posts=Post.objects.filter(title__contains=query)
    else:
        posts=Post.objects.filter(post_field=field)
    context={'posts':posts}
    return render(request,'home.html',context)


def about_dev(request):
    history=History.objects.filter(session_key=request.session.session_key)
    context={'history':history}
    return render(request, 'about.html',context)

def category(request,field):
    posts=Post.objects.filter(post_field=field)
    context={'posts':posts}
    return render(request,'home.html',context)

def delete(request,key):
    post=Post.objects.get(post_id=key)
    post.delete()
    return redirect('about_dev')

def like(request,post_id):
    
    post=Post.objects.get(post_id=post_id)
    session_key=request.session.session_key
    if Like.objects.filter(session_key=session_key,post=post).exists():
        #Like.objects.filter(session_key=session_key,post=post).delete()
        pass
        
    else:
        like=Like()
        like.session_key=session_key
        like.post=post
        like.save()
    post=post_id
    likes=Like.objects.filter(post=post)
    like_count=likes.count()
    dislikes=DisLike.objects.filter(post=post)
    dislike_count=dislikes.count()
    views=Views.objects.filter(post=post,status='positive')
    post=Post.objects.get(post_id=post)
    
    #context={'post':post,'likes':likes,'like_count':like_count}
    if request.method=='POST':
        comment=request.POST['comment']
        post=request.POST['post']
        post=Post.objects.get(post_id=post)

        view=Views()
        view.comment=comment
        view.status='positive'
        view.post=post
        view.session_key=request.session.session_key
        view.save()
        views=Views.objects.filter(post=post,status='positive')
    context={'post':post,'likes':likes,'views':views,'like_count':like_count,'dislike_count':dislike_count}
    


    return render(request,'individual.html',context)

        
 
   
def dislike(request,post_id):
    
    post=Post.objects.get(post_id=post_id)
    session_key=request.session.session_key
    if DisLike.objects.filter(session_key=session_key,post=post).exists():
        #DisLike.objects.get(session_key=session_key,post=post).delete()
        pass


    else:
        dislike=DisLike()
        dislike.session_key=session_key
        dislike.post=post
        dislike.save()
    post=post_id
    likes=Like.objects.filter(post=post)
    like_count=likes.count()
    dislikes=DisLike.objects.filter(post=post)
    dislike_count=dislikes.count()
    views=Views.objects.filter(post=post,status='negative')
    post=Post.objects.get(post_id=post)
    
    #context={'post':post,'likes':likes,'like_count':like_count}
    if request.method=='POST':
        comment=request.POST['comment']
        post=request.POST['post']
        post=Post.objects.get(post_id=post)

        view=Views()
        view.comment=comment
        view.status='negative'
        view.post=post
        view.session_key=request.session.session_key
        view.save()
        views=Views.objects.filter(post=post,status='negative')
    context={'post':post,'dislikes':dislikes,'views':views,'like_count':like_count,'dislike_count':dislike_count,}
    


    return render(request,'individual1.html',context)
    