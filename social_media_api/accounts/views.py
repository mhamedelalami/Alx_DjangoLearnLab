from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import UserProfileSerializer

# Follow a user
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser.objects.all(), id=user_id)
        request.user.following.add(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

# Unfollow a user
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser.objects.all(), id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)
