from django.contrib import admin
from.models import WallSection, UserContribution, HistoricalEvent, UserProfile  # 这里的.代表当前应用目录

admin.site.register(WallSection)
admin.site.register(HistoricalEvent)  # 注册历史事件模型到admin后台