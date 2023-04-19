from django.contrib.auth.models import User
from .models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile')

    def create(self, validated_data):
        """
        Make necessary modifications as per your requirements
        """
        profile_validated_data = dict(validated_data['profile'])
        print(profile_validated_data)
        nvd = validated_data.copy()
        nvd.pop("profile")
        print(nvd)
        create = super().create(validated_data=nvd)
        print(create.id)
        profile_validated_data.update({'user': create})
        user_profile = ProfileSerializer.create(ProfileSerializer(), profile_validated_data)
        # profile, created = Profile.objects.create(profile=user_profile)
        return create