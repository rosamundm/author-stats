from rest_framework import serializers
from .models import CustomUser


class CustomUserSeralizer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    last_updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "password",
        ]