"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from TestCase.views import home_view, load_clients, load_testcases, single_slug, index_view, updateStep, register, \
    login_app, logout_from_app,createOrder,deleteStep

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', index_view, name='homepage'),
    path('register/', register, name='register'),
    path('login/', login_app, name='login'),
    path('logout/', logout_from_app, name='logout'),
    path('home/', home_view, name='home_view'),
    path("home/<single_slug>", single_slug, name="single_slug"),
    path('load-clients/', load_clients, name='ajax_load_clients'),
    path('load-testcases/', load_testcases, name='load_testcases'),
    path('home/<single_slug>/<str:pk>/', updateStep, name='update_step'),
    path('home/create-step/<single_slug>', createOrder, name='create_step'),
    path('home/<single_slug>/<str:pk>', deleteStep, name='delete_step'),
    path('api/', include('TestCase.urls'))
]
