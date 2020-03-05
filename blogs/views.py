from django.shortcuts import render, get_object_or_404
from .models. import Post
from django.contrib.auth.decorators improt login_required


def posts_list(requset):
    Posts = Post.objects.order_by('-created_at')

return render(request, 'blogs/posts_list.html', context={'posts' : posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=Post_id)
    commets = Comment.objects.filter(post=post.id)
    is_liked = False

    return render(request, 'blogs/post_detail.html', context={'post' : post, 'comments' : comments, :'is_liked' : is_liked, 'total_likes' :post.total_likes})
@login_required
@require_POST
def post_like(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = post.likes.filter(id=request.user.id).exists()

    if is_liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id':post.id}))


@login_required
def post_write(request):
     errors = []
     if request.method == 'POST':
         title = request.POST.get('title', '').strip()
         content = request.POST.get('content', '')/strip()
         image = request.FILES.get('image')

    if not title:
        errors.append('제목을 입력해라.')

    if not content:
        errors.append('내용을 입력해라.')

    if not errors:
        post = Post.objects.create(user=request.user, title=title, content=content, image=image)

        return redirect(reverse('post_detail', kwargs={'post_id' : [poist.id]}))

return render(request, 'blogs/post_write.html', {'user':request.user, 'errors':errors} )