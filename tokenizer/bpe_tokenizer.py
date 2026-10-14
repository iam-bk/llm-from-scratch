class BPETokenizer:
    def __init__(self, token_sep: str = '_'):
        self.token_sep = token_sep
        self.unknown_token = "<|unk|>"
        self.unknown_token_id = 0
        self.token_to_id = {self.unknown_token: 0}
        self.id_to_token = {0: self.unknown_token}
        self.merged = []

    def _normalize(self, text: str) -> str:
        return text.strip().replace(' ', self.token_sep)

    def count(self, tokens):
        counts = {}
        for a, b in zip(tokens, tokens[1:]):
            if a.endswith(self.token_sep):  # don't merge across words
                continue
            counts[(a, b)] = counts.get((a, b), 0) + 1
        return counts

    def replace(self, tokens, pair):
        merged, i = [], 0
        while i < len(tokens):
            if i < len(tokens) - 1 and (tokens[i], tokens[i + 1]) == pair:
                merged.append(tokens[i] + tokens[i + 1])
                i += 2
            else:
                merged.append(tokens[i])
                i += 1
        return merged

    def merge(self, text: str, num_rounds: int = 20):
        tokens = list(self._normalize(text))
        self.chars = sorted(set(tokens))
        for _ in range(num_rounds):
            pairs = self.count(tokens)
            if not pairs:
                break
            best = max(pairs, key=pairs.get)
            tokens = self.replace(tokens, best)
            self.merged.append(best)

    def build_vocabulary(self):
        for token in self.chars + [a + b for a, b in self.merged]:
            if token not in self.token_to_id:
                tid = len(self.token_to_id)
                self.token_to_id[token] = tid
                self.id_to_token[tid] = token

    def encode(self, text: str):
        tokens = list(self._normalize(text))
        for pair in self.merged:
            tokens = self.replace(tokens, pair)
        return [self.token_to_id.get(t, self.unknown_token_id) for t in tokens]

    def decode(self, ids):
        return "".join(self.id_to_token[i] for i in ids).replace(self.token_sep, ' ')



