from rest_framework import serializers

from notes.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['username', 'bio', 'email']

    def get_username(self, obj):
        return obj.user.first_name

    def get_email(self, obj):
        return obj.user.email