from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.validators import ValidationError
from apps.user.models import User


class LogoutSerializer(serializers.Serializer):

    refresh = serializers.CharField()

    def validate(self, attrs):
        self.refresh = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.refresh).blacklist()

        except TokenError:
            raise ValidationError({'refresh': 'Token falso'})

    def create(self, validated_data):
        super().create(validated_data)

    def update(self, instance, validated_data):
        super().update(instance,validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',
                  'password', 'email', 'rol', 'is_superuser')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            email=validated_data["email"],
            last_name=validated_data['last_name'],
            is_superuser=validated_data['is_superuser'],
            rol=validated_data['rol'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if validated_data.get('username'):
            instance.username = validated_data['username']
        if validated_data.get('email'):
            instance.username = validated_data['email']
        if validated_data.get('first_name'):
            instance.first_name = validated_data['first_name']
        if validated_data.get('last_name'):
            instance.last_name = validated_data['last_name']
        if validated_data.get('is_superuser'):
            instance.is_superuser = validated_data['is_superuser']
        if validated_data.get('rol'):
            instance.rol = validated_data['rol']
        if validated_data.get('password'):
            instance.set_password(validated_data['password'])
        instance.save()
        return instance


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
        }


class MediumUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
        }
