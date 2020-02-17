import string

sentence = 'The happy puppy jumped on his owner, Bill, and barked with joy.';
translator = str.maketrans("","", string.punctuation)
sentence = sentence.translate(translator)
sentence = sentence.lower()
print(sentence)

STOP_WORDS = [
  'the', 'and'
]
words = sentence.split()
new_sentence = list(filter(lambda w: w not in STOP_WORDS, words))

print(new_sentence)
