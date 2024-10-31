#!/usr/bin/env python3
"""Module implementing a cache eviction policy: Most Recently Used (MRU).
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Defines a cache with a Most Recently Used (MRU) policy.
    When the cache reaches its maximum capacity, the most recently accessed item is removed first.
    """
    def __init__(self):
        """Set up the cache using an ordered dictionary.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Store an item in the cache.
        If adding the item exceeds the cache limit, the most recently used item is removed.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)  # Remove most recent item
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Access an item by key from the cache.
        Returns None if the key is not found.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)  # Update order on access
        return self.cache_data.get(key, None)
