LLM (Large Language Models):

LLMs are generally known as generative AI models. Some of these models are GPTAstra, Claude Opus, Fable, Gemini Argon and ... 

I am trying to build a LLM from the scratch, in the previous blog post, we discussed about Neural network and the core concepts of building a LLM. To start with in this blog post, we will talk about Tokenizer. 

What is Tokenizer?

How do we interact with a LLM model? Through Natural Language, in any language. 

But machines can only understand zeros and ones. 

"யாதும் ஊரே யாவரும் கேளிர்"

Can machine understand this text directly and respond ? - No

For machine to understand the text, we need to convert the text into numbers. 

Let's take a simple word:

"I love the nature"

What are the ways, we can break this sentence:

char by character = ['I', ' ', 'l', 'o', 'v', 'e', ' ', 't', 'h', 'e', ' ', 'n', 'a', 't', 'u', 'r', 'e']
word by word (consider space) = ['I', 'love', 'the', 'nature']
using the whole sentence = ["I love the nature"]
using bytes = [73, 32, 108, 111, 118, 101, 32, 116, 104, 101, 32, 110, 97, 116, 117, 114, 101]

LLMs are autoregressive models, that means the previous output, should be passed as an input.

There are many ways, we can break a given text into tokens. What is effective, if use character or bytes, the no of iterations will be long, vocabulary size will be huge, and there is no meaning for the tokens. 

Word tokenizer, word tokenizer is good, but the problem being unlike english, there is no clear separator for a word, and words like "Be", "Care", "Being", "Caring", "Spot", "Spotted", "Apologize", "Apology" we need more tokens to represent the same meaning words, and also it will not handle unknown words effectively. 

Most of modern LLM models, use a middle ground approach, called subword tokenizer. 

Apologize becomes ["Apolog", "ize"]
Aplogy becomes ["Apolog", "y"]

BPE (Byte Pair Encoding) is one of the most common methods used.  From the training text dataset, it counts frequently appearing pairs of characters, merge, and continue the same, to build a token vocabulary. 


