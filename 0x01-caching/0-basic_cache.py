#!/usr/bin/env python3
"""Basic cache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """This class inherits from BaseCaching and is a caching system"""
    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
