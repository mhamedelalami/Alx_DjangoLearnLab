from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    
    Fields:
        - bio: Optional text field for user biography.
        - profile_picture: Optional image field for user's profile picture.
        - followers: Many-to-many relationship to itself for user follow system.
                     'symmetrical=False' allows distinction between followers and following.
                     'related_name="following"' allows access to users this user follows.
    """
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username

    def follow(self, user):
        """
        Follow another user.
        """
        if user != self:
            self.following.add(user)

    def unfollow(self, user):
        """
        Unfollow a user.
        """
        if user != self:
            self.following.remove(user)

    def is_following(self, user):
        """
        Check if current user is following another user.
        """
        return self.following.filter(id=user.id).exists()

    def is_followed_by(self, user):
        """
        Check if current user is followed by another user.
        """
        return self.followers.filter(id=user.id).exists()
