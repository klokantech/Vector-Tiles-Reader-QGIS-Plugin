# -*- coding: utf-8 -*-
#
# This code is licensed under the GPL 2.0 license.
#
import unittest
import coverage
import sys


def get_tests():
    from test_mbtiles_source import MbtileSourceTests
    from test_tilehelper import TileHelperTests
    from test_vtreader import IfaceTests
    from test_tilejson import TileJsonTests

    tests = [
        unittest.TestLoader().loadTestsFromTestCase(MbtileSourceTests),
        unittest.TestLoader().loadTestsFromTestCase(TileHelperTests),
        unittest.TestLoader().loadTestsFromTestCase(IfaceTests),
        unittest.TestLoader().loadTestsFromTestCase(TileJsonTests)
    ]
    return tests


# run all tests using unittest skipping nose or testplugin
def run_all():
    cov = coverage.Coverage(omit=['*/usr/*', '*global_map_tiles*', '/vector-tiles-reader/tests/*', '*__init__.py'])
    cov.start()
    complete_suite = unittest.TestSuite(get_tests())
    print("")
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(complete_suite)
    print("")
    cov.stop()
    cov.save()
    cov.html_report(directory='tests/htmlcov')
    print cov.report()


if __name__ == "__main__":
    run_all()