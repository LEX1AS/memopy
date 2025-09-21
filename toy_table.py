# toy_table.py
from typing import Optional, List, Tuple, Any
import math

class ChainingHashTable:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]  # list of lists

    def simple_hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        idx = self.simple_hash(key)
        # update if exists
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return idx, i, 1
        # otherwise append
        self.buckets[idx].append((key, value))
        return idx, len(self.buckets[idx]) - 1, len(self.buckets[idx])

    def find(self, key):
        idx = self.simple_hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        raise KeyError

    def state(self):
        return [(i, list(self.buckets[i])) for i in range(self.capacity)]


class OpenAddressingHashTable:
    def __init__(self, capacity=16, probing='linear'):
        self.capacity = capacity
        self.slots = [None] * capacity
        self.keys = [None] * capacity
        self.probing = probing  # 'linear', 'quadratic', or 'double'
        self.size = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def _probe_sequence(self, base):
        # yield successive indices for probing
        if self.probing == 'linear':
            i = base
            while True:
                yield i % self.capacity
                i += 1
        elif self.probing == 'quadratic':
            i = 0
            while True:
                yield (base + i*i) % self.capacity
                i += 1
        elif self.probing == 'double':
            # second hash must be non-zero; use 1 + (hash2 % (capacity-1))
            h2 = 1 + (hash("salt") ^ base) % (self.capacity - 1)
            i = 0
            while True:
                yield (base + i * h2) % self.capacity
                i += 1
        else:
            raise ValueError("unknown probing")

    def insert(self, key, value):
        if self.size >= self.capacity:
            raise Exception("table full; implement resizing in real scenario")
        base = self._hash(key)
        probes = 0
        for idx in self._probe_sequence(base):
            probes += 1
            if self.slots[idx] is None:
                self.slots[idx] = value
                self.keys[idx] = key
                self.size += 1
                return idx, probes
            if self.keys[idx] == key:
                self.slots[idx] = value
                return idx, probes

    def find(self, key):
        base = self._hash(key)
        for idx in self._probe_sequence(base):
            if self.slots[idx] is None:
                raise KeyError
            if self.keys[idx] == key:
                return self.slots[idx]

    def state(self):
        return [(i, self.keys[i], self.slots[i]) for i in range(self.capacity)]
