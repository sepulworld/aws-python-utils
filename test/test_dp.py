import unittest
from unittest.mock import MagicMock
from aws_python_utils.datapipeline import datapipeline


class TestDataPipelineUtil(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_get_name(self):
        pipelines = datapipeline.get_by_name()
        self.assertIsNotNone(pipelines, "pipelines were not found")

    if __name__ == '__main__':
        unittest.main()