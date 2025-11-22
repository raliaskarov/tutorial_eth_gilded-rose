import unittest
from item import Item
from gilded_rose import GildedRose

class GildedRoseTest(unittest.TestCase):
    """
    Test suite for Gilded Rose kata.
    """

    def test_normal_item_before_sell_date(self):
        items = [Item("Elixir of the Mongoose", sell_in=10, quality=20)]
        shop = GildedRose(items)
        shop.update_quality()
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 19)

    def test_normal_item_on_sell_date(self):
        items = [Item("Elixir of the Mongoose", sell_in=0, quality=10)]
        shop = GildedRose(items)
        shop.update_quality()
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 8)

    def test_aged_brie_increases_quality(self):
        items = [Item("Aged Brie", sell_in=2, quality=0)]
        shop = GildedRose(items)
        shop.update_quality()
        self.assertEqual(items[0].sell_in, 1)
        self.assertEqual(items[0].quality, 1)

    def test_aged_brie_increases_twice_after_expiry(self):
        items = [Item("Aged Brie", sell_in=0, quality=10)]
        shop = GildedRose(items)
        shop.update_quality()
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 12)

    def test_aged_brie_quality_capped_at_50(self):
        cases = [
            (5, 50, 50),   # stays at cap before expiry
            (0, 50, 50),   # stays at cap on sell date even with +1 then +1
        ]
        for sell_in, start_q, expected_q in cases:
            with self.subTest(sell_in=sell_in, start_q=start_q):
                items = [Item("Aged Brie", sell_in=sell_in, quality=start_q)]
                shop = GildedRose(items)
                shop.update_quality()
                self.assertEqual(items[0].quality, expected_q)

    def test_sulfuras_constant(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        shop = GildedRose(items)
        shop.update_quality()
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 80)

    def test_conjured_items_double_degradation_pre_expiry(self):
        items = [Item("Conjured Mana Cake", sell_in=3, quality=6)]
        shop = GildedRose(items)
        shop.update_quality()
        self.assertEqual(items[0].sell_in, 2)
        self.assertEqual(items[0].quality, 4)

    def test_conjured_items_total_minus_four_on_sell_date(self):
        items = [Item("Conjured Mana Cake", sell_in=0, quality=10)]
        shop = GildedRose(items)
        shop.update_quality()
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 6)

if __name__ == '__main__':
    unittest.main()
