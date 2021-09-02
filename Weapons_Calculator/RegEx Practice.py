import re
import wikipedia

page = wikipedia.page('Cetiosauriscus')

text = page.content

print(text)

match = re.finditer(text)
