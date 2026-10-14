import re

class WordTokenizer:
    def __init__(self, text: str):
        self.unknown_token, self.unknown_token_id = "<|unk|>", 0
        self.token_to_id = {self.unknown_token: 0}
        self.id_to_token = {0: self.unknown_token}
        for word in self._split(text):
            if word not in self.token_to_id:
                tid = len(self.token_to_id)
                self.token_to_id[word] = tid
                self.id_to_token[tid] = word

    def _split(self, text):
        return re.findall(r"[\w']+|[^\w\s]", text.lower())

    def encode(self, text):
        return [self.token_to_id.get(w, self.unknown_token_id) for w in self._split(text)]

    def decode(self, ids):
        return " ".join(self.id_to_token[i] for i in ids)



