# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from app.members.models import Member


class MembersViews(APIView):

    def get_single_object(self, hashmail):
        return get_object_or_404(Member.objects.all(), hashmail=hashmail)

    def get(self, request, hashmail):
        member = self.get_single_object(hashmail)

        return Response({}, status=status.HTTP_200_OK)
