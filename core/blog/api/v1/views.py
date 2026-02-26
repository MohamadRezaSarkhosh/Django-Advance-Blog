from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializers


@api_view()
def postList(request):
    return Response({"name" : "MohamadReza"})


@api_view()
def postDetail(request, id):
    post = Post.objects.get(pk=id)
    serializers = PostSerializers(post)
    return Response(serializers.data)