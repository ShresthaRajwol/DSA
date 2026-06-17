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

        return node.meaning if node.is_end else None

    # ---------------- PREFIX SEARCH ----------------

    def _dfs(self, node, prefix, results):
        """Collect all words under this node"""
        if node.is_end:
            results.append((prefix, node.meaning))

        for ch, child in node.children.items():
            self._dfs(child, prefix + ch, results)

    def starts_with(self, prefix):
        """Returns all words + meanings that start with prefix"""
        node = self.root
        prefix = prefix.lower()

        # 1. Navigate to prefix node
        for ch in prefix:
            if ch not in node.children:
                return []   # no matches
            node = node.children[ch]

        # 2. DFS from that node
        results = []
        self._dfs(node, prefix, results)

        return results