from django.contrib import admin
from django.urls import include, path
from post import urls as post_urls
from user import urls as user_urls
from comment import urls as comment_urls
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(post_urls)),
    path('', include(user_urls)),
    path('', include(comment_urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', obtain_auth_token, name='token'),
]