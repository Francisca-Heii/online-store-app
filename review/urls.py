
from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_page, name='review'),
    path('feedback', views.feedback, name='review/feedback'),
]
