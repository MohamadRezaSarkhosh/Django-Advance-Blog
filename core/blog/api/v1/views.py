from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializers
from django.shortcuts import get_object_or_404

@api_view()
def postList(request):
    posts = Post.objects.filter(status=True)
    serializer = PostSerializers(posts,many=True)
    return Response(serializer.data)


@api_view()
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    serializers = PostSerializers(post)
    return Response(serializers.data)