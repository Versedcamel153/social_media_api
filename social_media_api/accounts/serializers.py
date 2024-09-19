from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'bio', 'profile_pic', 'followers'
        ]

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if username and password:
            user = authenticate(
                username=username,
                password=password,
            )
        elif email and password:
            user = authenticate(
                email=email,
                password=password
            )
        else:
            raise serializers.ValidationError('Must include either a "username" or "email" and a "password".')
        
        if user:
            if user.is_active:
                data['user'] = user
            else:
                raise serializers.ValidationError('User account disabled')
        else:
            raise serializers.ValidationError('Unable to log in with provided credentials')
        return data
    