#!/usr/bin/env python3
"""Module for implementing a Least Frequently Used (LFU) cache system.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Defines an LFU (Least Frequently Used) cache.
    Removes items based on the least frequency of access when the cache limit is exceeded.
    """
    def __init__(self):
        """Set up the LFU cache and initialize frequency tracking.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []  # Track key access frequencies

    def __reorder_items(self, key):
        """Reorder the cache entries to maintain least frequently used order.
        Updates positions based on the specified key's usage.
        """
        max_positions = []
        key_freq = 0
        key_pos = 0
        insert_pos = 0

        for i, entry in enumerate(self.keys_freq):
            if entry[0] == key:
                key_freq = entry[1] + 1  # Increment frequency for this access
                key_pos = i
                break
            elif not max_positions:
                max_positions.append(i)
            elif entry[1] < self.keys_freq[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()

        for pos in max_positions:
            if self.keys_freq[pos][1] > key_freq:
                break
            insert_pos = pos

        self.keys_freq.pop(key_pos)
        self.keys_freq.insert(insert_pos, [key, key_freq])

    def put(self, key, item):
        """Insert an item into the cache.
        Removes the least frequently used item if cache capacity is exceeded.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item

            insert_index = len(self.keys_freq)
            for i, entry in enumerate(self.keys_freq):
                if entry[1] == 0:
                    insert_index = i
                    break
            self.keys_freq.insert(insert_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieve an item from the cache by key.
        If found, updates the frequency of access for the item.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
