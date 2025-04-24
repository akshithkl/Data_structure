class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True

    def search(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.is_end

# Input
trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("app"))  # True
print(trie.search("appl")) # False


# Time Complexity: O(m) for m = length of word
# Space Complexity: O(n * m)

