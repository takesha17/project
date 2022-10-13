from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import *

User = get_user_model()


class RegistrationAPIView(APIView):
    """View for registration user"""

    
    def post(self, request):
        data = request.data
        serializer = UserRegistrationSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)

            return Response(
                "New user was created. ",
                status=status.HTTP_201_CREATED,
            )

class ProfileAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        return Response(
                f"username: {user.username}",
                status=status.HTTP_201_CREATED,
            )

