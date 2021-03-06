from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from models import Post


# Create your views here.
def listofposts(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request ,"listofposts.html",{"posts":posts})


def postdetail(request, id):
    post=get_object_or_404(Post, pk=id)
    post.count +=1
    post.save()
    return render(request, "postdetail.html", {"post": post})