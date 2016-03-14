#!/usr/bin/env python
import unittest

# This line is important so flake8 must ignore this one
from app import views # flake8: noqa
from app import mulungwishi_app


class URLTest(unittest.TestCase):

    def setUp(self):
        self.client = mulungwishi_app.test_client()
        self.client.testing = True

    def test_invalid_url_page_not_found(self):
        result = self.client.get('/page/not/found')
        self.assertEqual(result.status_code, 404)

    def test_invalid_query(self):
        result = self.client.get('/query?no_content')
        self.assertEqual(result.status_code, 400)

    def test_invalid_query_empty(self):
        result = self.client.get('/query?content')
        self.assertEqual(result.status_code, 400)

    def test_invalid_query_no_value_assigned(self):
        result = self.client.get('/query?content=')
        self.assertEqual(result.status_code, 400)

    def test_invalid_query_none(self):
        result = self.client.get('/query?')
        self.assertEqual(result.status_code, 400)

    def test_valid_url(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

    def test_valid_query(self):
        result = self.client.get('/query?content=farmer_sms')
        self.assertEqual(result.status_code, 200)
