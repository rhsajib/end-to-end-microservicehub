from django.contrib import admin
from django.urls import path, include
# from . import settings
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/task_manager/', include('task_manager.urls', namespace='task_manager')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)