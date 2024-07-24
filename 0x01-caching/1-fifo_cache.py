#!/usr/bin/env python3
"""FIFOCache Module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """ Initialize the FIFOCache """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.keys_order.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.keys_order.pop(0)
                del self.cache_data[oldest_key]
                print("DISCARD:", oldest_key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
