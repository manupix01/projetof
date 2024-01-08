"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_nested import routers
from api.views import UserViewSet, PostViewSet
from django.contrib import admin
from django.urls import path, include

from api import views

router = routers.SimpleRouter()

router.register(r'users', views.UserViewSet)
router.register(r'todos', views.TodoViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'posts', views.PostViewSet)

users_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
users_router.register(r'users', views.UserViewSet)

todos_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
todos_router.register(r'todos', views.TodoViewSet)

posts_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
posts_router.register(r'posts', views.PostViewSet)

comments_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
comments_router.register(r'comments', views.CommentViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'', include(users_router.urls)),
   
]


