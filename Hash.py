class HashTable:
    def __init__(self, size=10):
        self.size = size
        # each bucket is a list for chaining
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        # Division method: ensure we map any hashable key to 0..size-1
        if isinstance(key, int):
            return key % self.size
        # for non-integers use Python's hash then division
        return abs(hash(key)) % self.size

    def insert(self, key, value):
        """Insert or update (key, value)."""
        idx = self._hash(key)
        bucket = self.table[idx]
        # if key exists, update
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        # otherwise append new pair
        bucket.append((key, value))

    def search(self, key):
        """Return value if found, else None."""
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Delete key if present. Returns True if deleted, False if not found."""
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return True
        return False

    def display(self):
        """Show internal buckets for debugging/visualization."""
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# --- Demo ---
if __name__ == "__main__":
    ht = HashTable(size=10)

    # Insert some items
    ht.insert(10, "ten")
    ht.insert(20, "twenty")
    ht.insert(3, "three")
    ht.insert("apple", {"color": "red"})
    ht.insert(30, "thirty")

    print("Table after inserts:")
    ht.display()

    # Search
    print("\nSearch 20 ->", ht.search(20))
    print("Search 'apple' ->", ht.search("apple"))
    print("Search 99 ->", ht.search(99))

    # Delete
    print("\nDelete 20 ->", ht.delete(20))
    print("Delete 99 ->", ht.delete(99))

    print("\nTable after deletes:")
    ht.display()
