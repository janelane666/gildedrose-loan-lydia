# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    #test -1 jour
    def test_gr(self):

        items = [
            Item("Aged Brie", "cheeses", 2, 0),
            Item("Sulfuras, Hand of Ragnaros", "collectors", 0, 80),
            Item("Backstage passes to a TAFKAL80ETC concert", "events", 15, 20),
            Item("Conjured Mana Cake", "others", 3, 6)
                ]

        for i in range(30):
            gilded_rose = GildedRose(items)
            gilded_rose.update_quality()
            print()
            print("Nous sommes le jour", i, ":")
            for x in range(len(items)):
                print("Le produit", items[x].name, "vaut", items[x].quality,".")
            # self.assertEqual("50", items[1].quality)

if __name__ == '__main__':
    unittest.main()
