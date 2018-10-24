import re

postingText = ''
with open('posting.txt', 'r') as posting:
    postingText = posting.read().replace('\n', ' ').replace('\t', ' ')

postingText = re.sub(r'([^\s\w]|_)+', ' ', postingText)
result = []
for a in list(postingText.split(' ')):
    if a.isalnum():
        result.append(a)
result = set(result)
print(result)
print(len(result))