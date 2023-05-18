from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from KRWAPIendpoint.customMixin import PermissionsPerMethodMixin

# Create your views here.
class UserViewSet(PermissionsPerMethodMixin, viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get_queryset(self):
        queryset = super(UserViewSet, self).get_queryset()
        if self.request.user.is_authenticated:
            return queryset.filter(id=self.request.user.id)
        return {}
    
    @authentication_classes([])
    @permission_classes((AllowAny, ))
    def create(self, request, *args, **kwargs):
        print('working')
        resp = super().create(request, *args, **kwargs)
        if resp.status_code >= 200 < 300:
            if resp.status_text == 'Created':
                user = User.objects.get(username=request.data['username'])
                user.set_password(request.data['password'])
                user.save()
                return resp
        return resp
    
    @action(detail=False, methods=['GET'], serializer_class=UserSerializer)
    def userdetail(self, request, *args, **kwargs):
        user = UserSerializer(User.objects.get(id=request.user.id)).data
        return Response(user)
    
    @action(detail=False, methods=['GET'], serializer_class=ProfileSerializer)
    def update_profile_completion(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        print("request: "+str(request))
        try:
            profile = Profile.objects.get(user=user.id)
            profile.profile_form_filled = True
            profile.save()
            profile2 = ProfileSerializer(Profile.objects.get(user=user.id)).data
            return Response(profile2)
        except Exception as e:
            resp = Response({"error": str(e)})
            resp.status_code = 400
            return resp

