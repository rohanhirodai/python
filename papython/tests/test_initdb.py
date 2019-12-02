import os
import unittest


class TestInitializeDB(unittest.TestCase):

    def test_usage(self):
        from ..scripts.initialize_db import main
        with self.assertRaises(SystemExit):
            main(argv=['foo'])

    def test_run(self):
        from ..scripts.initialize_db import main
        main(argv=['foo', 'development.ini'])
        self.assertTrue(os.path.exists('papython.sqlite'))
        os.remove('papython.sqlite')
