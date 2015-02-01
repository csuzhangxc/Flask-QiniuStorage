#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Tests for Flask-QiniuStorage.'''

import unittest
import urllib
from flask import Flask
from flask_qiniustorage import Qiniu

QINIU_ACCESS_KEY = 'QINIU_ACCESS_KEY'
QINIU_SECRET_KEY = 'QINIU_SECRET_KEY'
QINIU_BUCKET_NAME = 'QINIU_BUCKET_NAME'
QINIU_BUCKET_DOMAIN = 'QINIU_BUCKET_DOMAIN'


class FlaskQiniuStorageTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config.from_object(__name__)
        self.qiniu = Qiniu(self.app)

    def test_save(self):
        data = 'test_save'
        filename = 'test_save'
        ret, info = self.qiniu.save(data, filename)
        self.assertIsInstance(ret, dict)
        self.assertEqual(ret['key'], filename)
        self.assertIsNotNone(ret.get('hash'))

    def test_delete(self):
        data = 'test_delete'
        filename = 'test_delete'
        self.qiniu.save(data, filename)
        ret, info = self.qiniu.delete(filename)
        self.assertIsInstance(ret, dict)
        self.assertFalse(ret)

    def test_url(self):
        data = 'test_url'
        filename = 'test_url'
        self.qiniu.save(data, filename)
        url = self.qiniu.url(filename)
        resp = urllib.urlopen(url)
        self.assertEqual(data, resp.read())


if __name__ == '__main__':
    unittest.main()