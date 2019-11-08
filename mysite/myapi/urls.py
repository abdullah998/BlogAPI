from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('posts',views.blog_post_set)

app_name='myapi'

urlpatterns=[
    path('',include(router.urls)),
    path('posts2',views.api.as_view()),
    path('posts3',views.api2.as_view()),
    path('posts4',views.api3.as_view()),
]
