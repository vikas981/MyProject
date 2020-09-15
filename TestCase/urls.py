from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("Module", views.moduleapi)
router.register("Client", views.clientapi)
router.register("Testcase",views.testcaseapi)
router.register("Testcasedetail",views.testcasedetailapi)


urlpatterns = [

    url('', include(router.urls)),


]