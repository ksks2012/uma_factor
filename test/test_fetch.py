import unittest

from input.fetch import HorseFetcher

class TestHorseFetcher(unittest.TestCase):
    def setUp(self) -> None:
        self.horse_fetcher = HorseFetcher()
        self.horse_fetcher.horse_name = "神鷹☆Numero1"
        self.horse_fetcher.blue = "智力"
        self.horse_fetcher.red = "中距離"
        self.horse_fetcher.green = ""
        self.horse_fetcher.exist_factor_idx = [46, 61, 0, 52, 67]
        self.horse_fetcher.stars = {'智力': 2, '路況差勁': 1, '彎道靈巧': 1, 'URA劇本': 1, '中距離': 1, '陰天': 1, '集中力': 1}
        self.horse_fetcher._gen_horse_info()
        return super().setUp()

    def test_horse_info(self):
        horse_info = self.horse_fetcher.horse_info
        print(horse_info)
        result = {'horse_name': '神鷹☆Numero1', 'blue': {'智力': 2}, 'red': {'中距離': 1}, 'white': {'路況差勁': 1, '彎道靈巧': 1, 'URA劇本': 1, '陰天': 1, '集中力': 1}}

        self.assertDictEqual(result, horse_info)