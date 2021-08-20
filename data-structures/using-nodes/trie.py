class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __iter__(self):
        words = self.get_all_words()
        for word in words:
            yield word[0]

    def __repr__(self):
        return " -> ".join(self)

    def auto_complete(self, prefix):
        current_node = self.search(prefix)
        if not current_node:
            return None
        return self.get_all_words_sorted(current_node)

    def search(self, word):
        current_node = self.root
        for c in word:
            if current_node.children.get(c):
                current_node = current_node.children[c]
            else:
                return None
        return current_node

    def get_all_words_sorted(self, node=None):
        words = self.get_all_words(node)
        return sorted(words, key=lambda x: x[1], reverse=True)

    def get_all_words(self, node=None, word="", words=None):
        if words is None:
            words = []
        current_node = node or self.root
        for key, child_node in current_node.children.items():
            if key == "*":
                words.append([word, child_node])
            else:
                self.get_all_words(child_node, word + key, words)
        return words

    def insert(self, word, score):
        if self.is_valid_score(score):
            current_node = self.root
            for c in word:
                if current_node.children.get(c):
                    current_node = current_node.children[c]
                else:
                    new_node = TrieNode()
                    current_node.children[c] = new_node
                    current_node = new_node
            current_node.children["*"] = score

    @staticmethod
    def is_valid_score(score):
        return (0 <= score) and (score <= 100)
