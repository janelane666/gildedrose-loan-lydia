# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        for item in self.items:
            if item.category == "collectors":
                item.quality = item.quality

            if item.category == "others": 
                    item.sell_in -=  1
                    item.quality -= 1
                    if item.sell_in < 0:
                        item.quality = 0

            if item.category == "cheeses" and item.quality < 50:
                    item.sell_in -= 1
                    item.quality += 2

            if item.category == "events" and item.quality < 50:
                item.sell_in -= 1
                if item.sell_in < 11:
                    item.quality += 2
                if item.sell_in < 6:
                    item.quality += 1
                if item.sell_in < 0:
                    item.quality = 0

   


'''
        for item in self.items:
            if item.category != "cheeses" and item.category != "events":
                if item.quality > 0:
                    if item.category != "collectors":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.category == "events":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.category != "collectors":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.category != "cheeses":
                    if item.category != "events":
                        if item.quality > 0:
                            if item.category != "collectors":
                                item.quality = item.quality - 1
                    else:
                        item.quality = 0
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
'''

class Item:
    def __init__(self, name, category, sell_in, quality):
        self.name = name
        self.category = category
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s, %s" % (self.name, self.category, self.sell_in, self.quality)
