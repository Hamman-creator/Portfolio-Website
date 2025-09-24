from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Experience
class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True, null=True)
    title_image = models.ImageField(upload_to="experiences/")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # null if still ongoing
    description = models.TextField()
    achievements = models.TextField(blank=True, null=True)  

    def __str__(self):
        return f"{self.title} at {self.company}"


# Projects
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    title_image = models.ImageField(upload_to="projects/")
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    technologies = models.CharField(
        max_length=255,
        help_text="Comma-separated list of technologies",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def tech_list(self):
        return [tech.strip() for tech in self.technologies.split(",") if tech.strip()]

    def __str__(self):
        return self.title




class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    title_image = models.ImageField(upload_to="blogs/")
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)  # fallback if user not logged in
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog.title}"




class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)  # required field
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"