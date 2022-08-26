from django.urls import path  # path would enable us add multiple urls in a list

from . import views

#add url patterns to take all the list in our projects

urlpatterns = [
    path('', views.index, name='index'), #this means home url
    path('blog', views.blog, name='blog'),
    path('blog/<str:pk>', views.blog, name='blog'), #url for the function blog

]
