from .models import ClickStatistics, UserRequests
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ClickStatisticsSerializer, UserRequestsSerializer


class ClickStatisticsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ClickStatistics.objects.all()
    serializer_class = ClickStatisticsSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserRequestsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = UserRequests.objects.all()
    serializer_class = UserRequestsSerializer
    permission_classes = [permissions.IsAuthenticated]
