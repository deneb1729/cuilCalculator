import unittest
from ..cuil_generator import generator

mock_cuils = [
    [36489026, "M", "20364890266"],
    [35824572, "M", "20358245723"],
    [8784875, "F", "27087848758"],
    [22621984, "M", "20226219847"],
    [35196499, "F", "27351964990"],
    [21578048, "F", "27215780487"],
    [18667907, "F", "27186679070"],
    [1823119, "M", "20018231191"],
    [14564917, "M", "20145649170"],
    [10009638, "F", "27100096388"],
    [37919086, "M", "20379190864"],
]


class TestCompleteCuil(unittest.TestCase):
    def test_complete_cuil(self):
        for element in mock_cuils:
            self.assertEqual(generator(element[0], element[1]), element[2])


if __name__ == "__main__":
    unittest.main()
