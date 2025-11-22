
import unittest
from item import Item
from gilded_rose import GildedRose

class GildedRoseTest(unittest.TestCase):
    """
    Test suite for Gilded Rose kata.
    """

    # Example Test:
    def test_normal_item_before_sell_date(self):
        """Normal item: before expiry, quality -1 and sell_in -1 after one update."""
        # Arrange
        items = [Item("Elixir of the Mongoose", sell_in=10, quality=20)]
        shop = GildedRose(items)

        # Act
        shop.update_quality()

        # Assert
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 19)

    def test_normal_item_on_sell_date(self):
        # TODO: Write test for normal item when sell_in == 0 (degrades twice overall)
        pass

    def test_aged_brie_increases_quality(self):
        # TODO: Write test for Aged Brie increasing by +1 before expiry
        pass

    def test_aged_brie_increases_twice_after_expiry(self):
        # TODO: Write test for Aged Brie increasing by +2 after expiry
        pass

    def test_aged_brie_quality_capped_at_50(self):
        # TODO: Write test(s) showing quality never exceeds 50
        pass

    def test_sulfuras_constant(self):
        # TODO: Write test verifying Sulfuras never changes sell_in or quality
        pass

    def test_conjured_items_double_degradation_pre_expiry(self):
        # TODO: Write test for Conjured items: -2 quality before expiry
        pass

    def test_conjured_items_total_minus_four_on_sell_date(self):
        # TODO: Write test for Conjured items on sell date: total -4 (today -2, then extra -2)
        pass


if __name__ == '__main__':
    unittest.main()
