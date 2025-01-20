from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Post, Comment, Like
from .forms import PostForm, CommentForm

# Create your views here.
def main(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "post/list.html", context)

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.writer = request.user
            newPost.save()
            return redirect('post:detail', newPost.id)
        else:
            return redirect('post:create')
    
    form = PostForm()
    context = {
        "form": form,
    }
    return render(request, 'post/create.html', context)

def detail(request, pk):
    post = Post.objects.get(id=pk)
    liking = Like.objects.filter(user=request.user, post=post).exists()
    likeCount = post.liker.count()
    commentCount = post.comment_set.count()
    
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    commentForm = CommentForm()
    context = {
        'post': post,
        'liking': liking,
        'likeCount': likeCount,
        'commentCount': commentCount,
        
        'comments': comments,
        'commentForm': commentForm,
    }
    return render(request, "post/detail.html", context)


# AJAX 요청으로 동작
def toggle_like(request, pk):
    post = Post.objects.get(id=pk)
    
    if request.method == "POST":
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        
        if created:
            # 새로 좋아요를 추가한 경우
            liked = True
        else:
            # 이미 좋아요가 존재하면 삭제 (좋아요 취소)
            like.delete()
            liked = False
            
        # 현재 게시글의 좋아요 개수
        like_count = post.liker.count()

        return JsonResponse({
            'liked': liked,
            'like_count': like_count,
        })
        
    return redirect("post:detail", pk)
    

# AJAX 요청으로 동작
def comment_create(request, post_pk):
    if request.method == "POST":
        post = Post.objects.get(id=post_pk)
        
        import json
        post_body = json.loads(request.body.decode("utf-8"))
        
        newComment = Comment.objects.create(
            post = post,
            writer = request.user,
            content = post_body.get('content')
        )            
            
        comment_count = post.comment_set.count()
        return JsonResponse({
            'writer_id' : newComment.writer.id,
            'content' : newComment.content,
            'created_at' : newComment.created_at,
            'comment_count': comment_count,
            'comment_id' : newComment.id
        })
        
    return redirect("post:detail", post_pk)

# AJAX 요청으로 동작
def comment_delete(request, post_pk, comment_pk):
    if request.method == "POST":
        post = Post.objects.get(id=post_pk)
        comment = Comment.objects.get(id=comment_pk)
        comment.delete()
        
        comment_count = post.comment_set.count()
        return JsonResponse({
            'comment_count': comment_count,
        })
        
    return redirect("post:detail", post_pk)
    