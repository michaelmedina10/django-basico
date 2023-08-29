from django.urls import path
from blog.views import blog_page, exemplo

# blog/
urlpatterns = [
    path('', blog_page),
    path('exemplo/', exemplo)
]