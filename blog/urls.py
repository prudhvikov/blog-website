from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('categories/',views.categories,name='categories'),
    path('<int:pk>/',views.details,name='details'),
    path('category/<int:id>',views.categories,name='category'),
]