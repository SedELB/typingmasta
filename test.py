from wonderwords import RandomWord
from wonderwords import RandomSentence

r = RandomWord()
s = RandomSentence()

sample_text = ""
for _ in range(5):
    sample_text += s.sentence() + '\n'

print(sample_text)
print(len(sample_text))