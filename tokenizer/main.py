from bpe_tokenizer import BPETokenizer
from word_tokenizer import WordTokenizer

text = """
	My name is Bharathi Kannan. I born and brought up in a small town near Villupuram. I love playing cricket.
"""

wtokenizer = WordTokenizer(text)
bpeTokenizer = BPETokenizer()
bpeTokenizer.merge(text)
bpeTokenizer.build_vocabulary()
text_to_be_encoded = "who is Bharathi Kannan"
print("-----BPE--------")
print(bpeTokenizer.encode(text_to_be_encoded))
print(bpeTokenizer.decode(bpeTokenizer.encode(text_to_be_encoded)))
print("----WORD TOKENIZER-------")
print(wtokenizer.encode(text_to_be_encoded))
print(wtokenizer.decode(wtokenizer.encode(text_to_be_encoded)))
