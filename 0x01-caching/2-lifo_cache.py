#!/usr/bin/env python3
"""LIFO caching module.
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implements a cache with LIFO (Last-In First-Out) eviction policy.
    Items are removed in reverse order of their addition when the cache limit is reached.
    """
    def __init__(self):
        """Initialize the cache as an ordered dictionary.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.
        If the cache exceeds the maximum size, the most recently added item is discarded.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieve an item from the cache by key.
        Returns None if the key is not in the cache.
        """
        return self.cache_data.get(key, None)
