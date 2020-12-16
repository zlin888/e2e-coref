import sentencepiece as spm
import json
import os
from data import process_example

input_file = ''

s = spm.SentencePieceProcessor()
s.Load('./xlnet_cased_L-12_H-768_A-12/spiece.model')

# Retrieve size
print(s.get_piece_size())
print(s.encode('this is a test'))

json_examples = []
for x in ['test', 'train', 'dev']:
    with open(os.path.join(input_file, x + '.english.jsonlines')) as f:
        json_examples.extend((json.loads(jsonline) for jsonline in f.readlines()))

orig_examples = []
bert_examples = []
for i, json_e in enumerate(json_examples):
    e = process_example(json_e, i, should_filter_embedded_mentions=True)
    orig_examples.append(e)
    print(s.encode(' '.join(e.tokens)))
    # bert_examples.append(e.bertify(tokenizer))
# for i in orig_examples: print(i.tokens)