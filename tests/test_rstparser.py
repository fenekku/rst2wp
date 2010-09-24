import nodes
import mock
try:
    import unittest2 as unittest
except ImportError:
    import unittest  # and hope for the best

from docutils import core

class TestNodes(unittest.TestCase):
    def test_field_loader(self):
        text = """
:title: Hello
:foo: - test1
      - test2
      - test3

This is a test."""

        fields = {}

        output = core.publish_parts(source=text,
                                    settings_overrides = {'fields': fields})

        self.assertEqual(fields['title'], 'Hello')
        self.assertEqual(fields['foo'], ['test1', 'test2', 'test3'])
