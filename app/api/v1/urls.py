# -*- coding: utf-8 -*-

from rest_framework import routers

from django.conf.urls import patterns, url

from app.api.v1.members import MembersViews

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'^members/([0-9a-zA-Z]{32})/status$', MembersViews.as_view(), name='member-status')
]

urlpatterns += router.urls
