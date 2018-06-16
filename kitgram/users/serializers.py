from rest_framework import serializers
from . import models

class ExploreUserSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.User
    field = (
      'profile_image',
      'username',
      'name',
    )
