class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        """Generate a hash for the key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        if not self.table[index]:
            self.table[index] = [(key, value)]
        else:
            for idx, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][idx] = (key, value)
                    return
            self.table[index].append((key, value))

    def search(self, key):
        """Search for a value by its key."""
        index = self._hash(key)
        if self.table[index]:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        """Delete a key-value pair by key."""
        index = self._hash(key)
        if self.table[index]:
            for idx, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][idx]
                    return True
        return False

    def resize(self):
        """Resize the hash table (double its size)."""
        self.size *= 2
        old_table = self.table
        self.table = [None] * self.size
        for bucket in old_table:
            if bucket:
                for key, value in bucket:
                    self.insert(key, value)

# Example usage
ht = HashTable()
ht.insert('apple', 10)
ht.insert('banana', 20)
ht.insert('grape', 30)
print("Search for 'banana':", ht.search('banana'))
ht.delete('apple')
print("After Deletion, Search for 'apple':", ht.search('apple'))
ht.resize()
print("After Resize, Search for 'banana':", ht.search('banana'))