from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    target_repr = serializers.SerializerMethodField()  # new field

    class Meta:
        model = Notification
        fields = [
            'id', 
            'recipient', 
            'actor', 
            'actor_username', 
            'verb', 
            'target_repr',  # instead of raw target
            'timestamp',
            'is_read'
        ]

    def get_target_repr(self, obj):
        if obj.target is not None:
            # Customize this to show whatever you want for the target
            return str(obj.target)  # calls __str__ of the target model
        return None
