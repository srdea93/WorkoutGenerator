
import re

def regex_search(pattern, list):
    search = re.findall(pattern=pattern, string=list)
    return search

list = ["pushup", "situp", "push away", "jumping jacks", "close pushup"]
pattern = "pus"
search = regex_search(pattern, list)
print(search)
