from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    date_joined = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        read_only=True
    )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "date_joined",
        ]
        read_only_fields = ["id", "date_joined"]
