# -*- coding: utf-8 -*-

from model_mommy import mommy

from django.test import TestCase
from django.core.urlresolvers import reverse_lazy


class MemberViewsTestCase(TestCase):

    def setUp(self):
        self.member = mommy.make('members.Member')

    def test_get_member_by_hashsum_status_ok(self):
        response = self.client.get(reverse_lazy('api-v1:member-status', args=[self.member.hashmail]))

        self.assertEqual(response.status_code, 200)

    def test_get_member_by_hashsum_status_not_found(self):
        response = self.client.get(reverse_lazy('api-v1:member-status', args=['12345678901234567890123456789012']))

        self.assertEqual(response.status_code, 404)

    def test_get_member_by_hashsum_status_not_available(self):
        response = self.client.get(reverse_lazy('api-v1:member-status', args=[self.member.hashmail]))

        self.assertEqual(response.status_code, 422)
