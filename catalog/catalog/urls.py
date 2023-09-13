from django.contrib import admin
from django.urls import path, include



admin.site.site_header = 'Админка тестового задания Арлазаровой Натальи'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
