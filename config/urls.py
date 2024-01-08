from rest_framework_nested import routers
from api.views import UserViewSet, TodoViewSet, CommentViewSet, PostViewSet
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'todos', TodoViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'posts', PostViewSet)

users_router = routers.NestedDefaultRouter(router, r'users', lookup='user')
users_router.register(r'todos', TodoViewSet, basename='user-todos')
users_router.register(r'posts', PostViewSet, basename='user-posts')

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(users_router.urls)),
]
