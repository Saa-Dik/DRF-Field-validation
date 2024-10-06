
from django.contrib import admin
from django.urls import path, include
from rest_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    path('student-api/', views.StudentAPI.as_view()),
]
