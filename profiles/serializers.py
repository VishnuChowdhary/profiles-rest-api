from rest_framework import serializers
from profiles import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for our testing api"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validate_data):
        user = models.UserProfile.objects.create_user(
            email=validate_data['email'],
            name=validate_data['name'],
            password=validate_data['password']
        )
        return user