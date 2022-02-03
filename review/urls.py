
from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_page, name='review'),
    path('feedback', views.feedback, name='review/feedback'),
    path('contact', views.contactus, name='review/contact'),
    path('edit', views.edit_feedback, name='review/edit'),
    path('review_page', views.review_page, name='review/review_page'),
    path('delete', views.deleteDB, name='review/delete')



]
