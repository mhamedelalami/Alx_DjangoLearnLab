from rest_framework import generics, permissions, views, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Registration View
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

# Custom Login View to return token
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

# User Profile View
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# Follow another user
class FollowUserView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)
        if target_user == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target_user)
        return Response({"detail": f"You are now following {target_user.username}."}, status=status.HTTP_200_OK)

# Unfollow a user
class UnfollowUserView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(User, id=user_id)
        if target_user == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(target_user)
        return Response({"detail": f"You have unfollowed {target_user.username}."}, status=status.HTTP_200_OK)
