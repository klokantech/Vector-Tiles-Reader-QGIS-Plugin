import sys
import unittest
from util.tile_helper import *
import itertools


class TileHelperTests(unittest.TestCase):
    """
    Tests for Iface
    """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_change_scheme(self):
        self.assertEqual(0, change_scheme(zoom=0, y=0))
        self.assertEqual(0, change_scheme(zoom=1, y=1))
        self.assertEqual(166, change_scheme(zoom=8, y=89))
        self.assertEqual(2729017, change_scheme(zoom=22, y=1465286))

    def test_latlon_to_tile_tms(self):
        tms_tile = latlon_to_tile(0, WORLD_BOUNDS[1], WORLD_BOUNDS[0], source_crs=4326, scheme="tms")
        self.assertEquals((0, 0), tms_tile)

    def test_latlon_to_tile_xyz(self):
        xyz_tile = latlon_to_tile(0, WORLD_BOUNDS[1], WORLD_BOUNDS[0], source_crs=4326, scheme="xyz")
        self.assertEquals(xyz_tile, (0, 0))

    def test_get_zoom_by_scale_min(self):
        zoom = get_zoom_by_scale(-1)
        self.assertEqual(23, zoom)

    def test_get_zoom_by_scale_max(self):
        zoom = get_zoom_by_scale(10000000000)
        self.assertEqual(0, zoom)

    def test_get_epsg(self):
        self.assertEqual(3857, get_code_from_epsg("epsg:3857"))

    def test_world_bounds(self):
        tile = get_tile_bounds(zoom=14, bounds=WORLD_BOUNDS, source_crs=4326, scheme="xyz")
        bounds_expected = {'y_min': 0,
                           'y_max': 16383,
                           'zoom': 14,
                           'height': 16384,
                           'width': 16384,
                           'x_max': 16383,
                           'x_min': 0}
        self.assertEqual(bounds_expected, tile)

    def test_center_tiles(self):
        all_tiles = list(itertools.product(range(1, 6), range(1, 6)))
        t = get_tiles_from_center(nr_of_tiles=0, available_tiles=all_tiles)
        self.assertEqual(0, len(t))

    def test_center_tiles_difference(self):
        tile_limit = 4
        extent_a = {'y_min': 3, 'y_max': 5, 'zoom': 3, 'height': 3, 'width': 2, 'x_max': 4, 'x_min': 3}
        extent_b = {'y_min': 3, 'y_max': 6, 'zoom': 3, 'height': 4, 'width': 8, 'x_max': 7, 'x_min': 0}
        tiles_equal = center_tiles_equal(tile_limit=tile_limit, extent_a=extent_a, extent_b=extent_b)
        self.assertTrue(tiles_equal)


def suite():
    s = unittest.makeSuite(TileHelperTests, 'test')
    return s


# run all tests using unittest skipping nose or testplugin
def run_all():
    unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(suite())


if __name__ == "__main__":
    run_all()
