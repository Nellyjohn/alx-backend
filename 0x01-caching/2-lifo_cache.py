#!/usr/bin/env python3
"""LIFOCache module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a caching system using LIFO eviction policy """

    def __init__(self):
        """ Initialize the LIFOCache """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # LIFO: Discard the last item added
                last_key = list(self.cache_data.keys())[-2]
                del self.cache_data[last_key]
                print("DISCARD:", last_key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
