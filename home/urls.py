from django.urls import path
from .views import home_view
from . import views

urlpatterns = [
    path("", home_view, name="home"),
    path("about/", views.about, name="about"),
    path("experience/", views.experience, name="experience"),
    path("experience/<int:pk>/", views.experience_detail, name="experience_detail"),
    path("blogs/", views.blogs, name="blogs"),
    path("blogs/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("blogs/<int:pk>/like/", views.like_blog, name="like_blog"),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("contact/", views.contact, name="contact"),

]