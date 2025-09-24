from django.shortcuts import render, get_object_or_404, redirect
from .models import Experience, Project, Blog, Comment
from .forms import CommentForm,MessageForm
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
# Create your views here.

def home_view(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, "home/about.html")

def experience(request):
    experiences = Experience.objects.all().order_by("-start_date")
    return render(request, "home/experience.html", {"experiences": experiences})
def experience_detail(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    return render(request, "home/experience_detail.html", {"experience": experience})


def projects(request):
    projects = Project.objects.all().order_by("-created_at")
    return render(request, "home/projects.html", {"projects": projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "home/projects_detail.html", {"project": project})

def blogs(request):
    blogs = Blog.objects.all().order_by("-created_at")
    return render(request, "home/blogs.html", {"blogs": blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = blog.comments.all().order_by("-created_at")

    if request.method == "POST" and "comment_submit" in request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect("blog_detail", pk=blog.pk)
    else:
        form = CommentForm()

    return render(request, "home/blogs_detail.html", {
        "blog": blog,
        "comments": comments,
        "form": form,
    })


def like_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    liked_posts = request.session.get("liked_posts", [])

    if pk in liked_posts:
        # Unlike
        blog.likes -= 1
        liked_posts.remove(pk)
    else:
        # Like
        blog.likes += 1
        liked_posts.append(pk)

    blog.save()
    request.session["liked_posts"] = liked_posts
    request.session.modified = True

    return HttpResponseRedirect(reverse("blog_detail", args=[pk]))



def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})  # AJAX response
        return JsonResponse({"success": False, "errors": form.errors}, status=400)
    else:
        form = MessageForm()
    return render(request, "home/contact_form.html", {"form": form})