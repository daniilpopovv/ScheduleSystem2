from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('news/', HomeNews.as_view(), name='news'),
    path('news/<int:pk>', ViewNews.as_view(), name='view_news'),
    path('ScheduleSystem/<int:pk>/', ViewLessons.as_view(), name='view_lessons'),
]
