from rest_framework import serializers
from api.models import User, ActivityPeriod


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz')
