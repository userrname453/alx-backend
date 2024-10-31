#!/usr/bin/env python3
""" caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """an object  allows storing 
    retrieving items from a dictionary.
    """
    def put(self, key, item):
        """Adds item to the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves item by key.
        """
        return self.cache_data.get(key, None)
