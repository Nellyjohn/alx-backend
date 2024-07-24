#!/usr/bin/env python3
"""LFUCache module"""
from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
	""" LFUCache defines a caching system using LFU eviction policy """

	def __init__(self):
		""" Initialize the LFUCache """
		super().__init__()
		self.frequency = defaultdict(int)
		self.recently_used = OrderedDict()

	def put(self, key, item):
		""" Add an item to the cache """
		if key is not None and item is not None:
			if key in self.cache_data:
				self.frequency[key] += 1
			else:
				self.frequency[key] = 1

			self.cache_data[key] = item

			if key in self.recently_used:
				self.recently_used.move_to_end(key)
			else:
				self.recently_used[key] = item

			if len(self.cache_data) > BaseCaching.MAX_ITEMS:
				self._evict_least_frequently_used()

	def get(self, key):
		""" Get an item by key """
		if key in self.cache_data:
			self.frequency[key] += 1
			self.recently_used.move_to_end(key)
			return self.cache_data[key]
		return None

	def _evict_least_frequently_used(self):
		""" Evict the least frequently used item from the cache """
		least_freq = min(self.frequency.values())
		least_freq_keys = [k for k, v in self.frequency.items() if v == least_freq]

		if len(least_freq_keys) > 1:
			least_recently_used_key = None
			for k in self.recently_used:
				if k in least_freq_keys:
					least_recently_used_key = k
					break
			evict_key = least_recently_used_key
		else:
			evict_key = least_freq_keys[0]

		del self.cache_data[evict_key]
		del self.frequency[evict_key]
		del self.recently_used[evict_key]
		print("DISCARD:", evict_key)
