class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.meaning = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, meaning):
        node = self.root
        word = word.lower()

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_end = True
        node.meaning = meaning

    def search(self, word):
        node = self.root
        word = word.lower()

        for ch in word:
            if ch not in node.children:
                return None
            node = node.children[ch]

        if node.is_end:
            return node.meaning

        return None