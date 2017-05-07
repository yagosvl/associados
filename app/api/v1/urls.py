# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from app.api.v1.members import membersView
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'^members/([0-9a-zA-Z]){32}/status', membersView, basename='members')

urlpatterns += router.urls
