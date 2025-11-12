# very_simple_linear_probing.py

TOMBSTONE = object()

class SimpleHash:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size  # None = empty, TOMBSTONE = deleted, otherwise holds key

    def _hash(self, key):
        try:
            k = int(key)
        except Exception:
            k = abs(hash(key))
        return k % self.size

    def insert(self, key):
        if self.search(key) is not None:
            return False  # already present
        start = self._hash(key)
        for i in range(self.size):
            idx = (start + i) % self.size
            if self.table[idx] is None or self.table[idx] is TOMBSTONE:
                self.table[idx] = key
                return True
        return False  # table full

    def search(self, key):
        start = self._hash(key)
        for i in range(self.size):
            idx = (start + i) % self.size
            slot = self.table[idx]
            if slot is None:
                return None  # not found (probe stops)
            if slot is TOMBSTONE:
                continue
            if slot == key:
                return idx
        return None

    def delete(self, key):
        idx = self.search(key)
        if idx is None:
            return False
        self.table[idx] = TOMBSTONE
        return True

    def display(self):
        print("Index : Value")
        for i, v in enumerate(self.table):
            if v is None:
                print(f"{i:5} : EMPTY")
            elif v is TOMBSTONE:
                print(f"{i:5} : TOMBSTONE")
            else:
                print(f"{i:5} : {v}")

def run_cli():
    ht = SimpleHash(size=10)
    menu = "1) Insert  2) Search  3) Delete  4) Display  5) Exit"
    while True:
        print("\n" + menu)
        c = input("Choice: ").strip()
        if c == "1":
            k = input("Key to insert: ").strip()
            try:
                key = int(k)
            except:
                key = k
            ok = ht.insert(key)
            print("Inserted." if ok else "Insert failed (exists or full).")
        elif c == "2":
            k = input("Key to search: ").strip()
            try:
                key = int(k)
            except:
                key = k
            idx = ht.search(key)
            print(f"Found at index {idx}." if idx is not None else "Not found.")
        elif c == "3":
            k = input("Key to delete: ").strip()
            try:
                key = int(k)
            except:
                key = k
            ok = ht.delete(key)
            print("Deleted." if ok else "Key not found.")
        elif c == "4":
            ht.display()
        elif c == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run_cli()

