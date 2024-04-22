
# replace words with emojis
# this only works for one word emojis and singular

# https://pypi.org/project/emoji/
# https://www.unicode.org/emoji/charts/full-emoji-list.html
# https://carpedm20.github.io/emoji/

import emoji

# print("\U0001F62D")
# print(emoji.emojize(":grinning_face:"))
# print(emoji.emojize(":thumbs_up:"))

text = "This is a text which makes me :) and :(. I am from Germany. I like baby, elephant, cat, pineapple and rhinoceros."

# TODO: add more mappings
mapped = {':)': 'slightly_smiling_face', ':(': 'slightly_frowning_face'}

tags = []
f1 = open('emo.csv')
for line in f1:
  tags.append(line.split('\t')[1][1:-2]) # remove :

print(len(tags))
# print([tag for tag in tags if 'ele' in tag])

new_text = ''

for word in text.split(' '):
  if word[-1] in ['.', ',', '!', '?']:
  	word, punct = word[:-1], word[-1]
  else:
  	punct = ''
  if word in mapped:
  	word = mapped[word]
  if word in tags:
  	new_text += ':' + word + ':' + punct + ' '
  else:
  	new_text += word + punct + ' '

print(emoji.emojize(new_text))



