# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    #test -1 jour
    def test_cake_valide(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].quality)

    #test produit périmé
    def test_cake_perime(self):
        items = [Item("Conjured Mana Cake", -1, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_brie_present(self):
        items = [Item("Aged Brie", -5, 1)]  
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_brie(self):
        items = [Item("Aged Brie", 1, 0)]  
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

if __name__ == '__main__':
    unittest.main()
