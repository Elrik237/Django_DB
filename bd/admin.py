from django.contrib import admin
from .models import ClickStatistics, UserRequests

admin.site.register(ClickStatistics)
admin.site.register(UserRequests)
