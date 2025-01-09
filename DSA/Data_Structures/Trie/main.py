class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """Search for a word in the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def delete(self, word):
        """Delete a word from the Trie."""
        def _delete(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[index]
            if char not in node.children:
                return False
            can_delete_child = _delete(node.children[char], word, index + 1)
            if can_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            return False
        
        _delete(self.root, word, 0)

    def starts_with(self, prefix):
        """Return True if there is any word in the Trie that starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def display(self, node=None, prefix=''):
        """Display all words in the Trie."""
        if node is None:
            node = self.root
        if node.is_end_of_word:
            print(prefix)
        for char, child_node in node.children.items():
            self.display(child_node, prefix + char)

# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")
print("Search for 'apple':", trie.search("apple"))
print("Search for 'app':", trie.search("app"))
print("Search for 'banana':", trie.search("banana"))
trie.delete("app")
print("After Deletion of 'app':", trie.search("app"))
print("Words that start with 'ba':", trie.starts_with("ba"))

print("Words in Trie:")
trie.display()