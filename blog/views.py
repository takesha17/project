from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


# class PostAPIView(APIView):

#     def get(self, request):
#         posts 
#         aa = PostSerializer(posts,many=True).data
#         return Response(aa)


class PostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def get_queryset(self):
    #     print(Post.comments_set.all())
    #     return super().get_queryset()

        
        