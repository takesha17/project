from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


class PostAPIView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        aa = PostSerializer(posts,many=True).data
        return Response(aa)

        
        