from item import Item

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"

# Helper functions to reduce nesting and duplication
def is_conjured(name: str) -> bool:
    return name.startswith("Conjured")

def clamp(q: int) -> int:
    return 0 if q < 0 else 50 if q > 50 else q

def delta(name: str) -> int:
    if name == AGED_BRIE:
        return +1
    if is_conjured(name):
        return -2
    return -1  # normal

class GildedRose:
    """Gilded Rose inventory system; updates item qualities."""
    
    def __init__(self, items: list[Item]):
        self.items = items

    def update_quality(self) -> None:
        for it in self.items:
            if it.name == SULFURAS:
                continue

            # today's effect
            it.quality = clamp(it.quality + delta(it.name))

            # day passes
            it.sell_in -= 1

            # post-expiry effect
            if it.sell_in < 0:
                it.quality = clamp(it.quality + delta(it.name))
