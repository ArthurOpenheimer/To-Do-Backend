from django.contrib import admin
from django.urls import path, include
from todo.views import TodoViewSet, UserViewSet, TodosForUser
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todos', TodoViewSet, basename='todos')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('users/<int:pk>/todos', TodosForUser.as_view()),
]
