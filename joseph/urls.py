"""joseph URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views as main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.index, name="index"),
    path('books/', main.books, name="books"),
    path('donate/', main.donate, name="donate"),
    path('establishment/', main.establishment, name="establishment"),
    path('journal/', main.journal, name="journal"),
    path('se/', main.se, name="se"),
    path('testimonial/', main.testimonial, name="testimonial"),
    path('journal/<int:pk>/', main.journal_detail, name='journal_detail'),

]
