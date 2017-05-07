# -*- coding: utf-8 -*-

from model_mommy import mommy

from django.test import TestCase
from django.urls import reverse_lazy


class MemberViewsTestCase(TestCase):

    def setUp(self):
        self.member = mommy.make('members.Member')


    def test_get_member_by_hashsum_status_ok(self):
        response = self.client.get(reverse_lazy('api-v1:members-detail', args=[self.member.hashmail]))

        self.assertEqual(response.status_code, 200)
