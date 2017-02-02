"""project_source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Moodslider import views
from django.conf.urls.static import static
from django.conf import settings

"""
These are the URL patterns that are used on the website.
"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'file-upload/', views.file_upload, name='file_upload'),
    url(r'^ajax/process_mood/$', views.process_mood, name='process_mood'),
    url(r'^get-suggestions/', views.process_mood, name='suggestions')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
