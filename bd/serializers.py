from .models import ClickStatistics, UserRequests
from rest_framework import serializers


class ClickStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClickStatistics
        fields = ['time', 'f_name', 'user_id', 'user_name', 'user_fullname']


class UserRequestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRequests
        fields = ['user_id', 'user_name', 'user_fullname', 'time']

