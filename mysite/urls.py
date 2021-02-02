from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, ListView, DetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', TemplateView.as_view(template_name="polls/homepage.html")),
    path('homepage/', TemplateView.as_view(template_name="polls/homepage.html")),
    path('aboutme/', TemplateView.as_view(template_name="polls/aboutme.html")),
    path('previousWork/', TemplateView.as_view(template_name="polls/previousWork.html")),
    path('courseWork/', TemplateView.as_view(template_name="polls/courseWork.html")),
    #path('skills/', TemplateView.as_view(template_name="polls/skills.html")),
    #path('resume/', TemplateView.as_view(template_name="polls/resume.html")),
]
