from collections import deque
from functools import lru_cache


class LRUCache:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.queue = deque()
        self.hash_map = dict()

    def is_queue_full(self):
        return len(self.queue) == self.cache_size

    def set(self, key, value):
        if key not in self.hash_map:
            if self.is_queue_full():
                pop_key = self.queue.pop()
                self.hash_map.pop(pop_key)

            self.queue.appendleft(key)
            self.hash_map[key] = value

    def get(self, key):
        if key not in self.hash_map:
            return -1
        else:
            self.queue.remove(key)
            self.queue.appendleft(key)
            return self.hash_map[key]


@lru_cache(maxsize=3, typed=True)
def factorial(n):
    print(f"Level {n}")
    return 1 if n <= 1 else n * factorial(n - 1)


if __name__ == '__main__':
    lru = LRUCache(3)
    lru.set('a', 1)
    lru.set('b', 2)
    lru.set('c', 3)
    lru.set('d', 4)
    print(lru.get('a'))
    print(lru.get('b'))
    print(lru.get('c'))
    print(lru.get('d'))

    print('--- functools lru_cache ---')
    a = factorial(5)
    print(f'5! = {a}')
    b = factorial(3)
    print(f'3! = {b}')
