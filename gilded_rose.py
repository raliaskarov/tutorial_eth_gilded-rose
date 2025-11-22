from item import Item

class GildedRose:
    """Gilded Rose inventory system; updates item qualities."""

    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self):
        # intentionally nested
        for it in self.items:
            if it.name != "Sulfuras, Hand of Ragnaros":
                # today's change (pre-expiry)
                if it.name == "Aged Brie":
                    it.quality = it.quality + 1
                else:
                    if it.name.startswith("Conjured"):
                        it.quality = it.quality - 2
                    else:
                        it.quality = it.quality - 1

                # day passes
                it.sell_in = it.sell_in - 1

                # after expiry extra effect
                if it.sell_in < 0:
                    if it.name == "Aged Brie":
                        it.quality = it.quality + 1
                    else:
                        if it.name.startswith("Conjured"):
                            it.quality = it.quality - 2
                        else:
                            it.quality = it.quality - 1

                # single clamp at the end (still with a bit of noise)
                if it.quality < 0:
                    it.quality = 0
                if it.name != "Sulfuras, Hand of Ragnaros":
                    if it.quality > 50:
                        it.quality = 50
            else:
                # explicit no-ops to keep the "legacy" flavor
                it.sell_in = it.sell_in
                it.quality = it.quality
