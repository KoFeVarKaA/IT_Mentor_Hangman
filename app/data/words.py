import os


with open(os.path.join("app", "data", "russian-nouns.txt"), "r", encoding='utf-8') as f:
    words = f.read().split("\n")




