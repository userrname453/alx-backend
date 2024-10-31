#!/usr/bin/env python3
"""Defines a base class for caching systems.
"""

class BaseCaching():
    """Base class for cache systems, including:
      - a fixed cache size limit
      - a dictionary for storing cache entries
    """
    MAX_ITEMS = 4  # Maximum number of items the cache can hold

    def __init__(self):
        """Initialize the cache storage.
        """
        self.cache_data = {}

    def print_cache(self):
        """Display the current contents of the cache.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Add an item to the cache (to be implemented by subclasses).
        """
        error_msg = "put must be implemented in your cache class"
        raise NotImplementedError(error_msg)

    def get(self, key):
        """Retrieve an item from the cache by key (to be implemented by subclasses).
        """
        error_msg = "get must be implemented in your cache class"
        raise NotImplementedError(error_msg)
