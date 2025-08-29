with open("data/russian-nouns.txt", "r", encoding='utf-8') as f:
    words = f.read().split("\n")
    for i in range(len(words)):
        words[i] = words[i].split("\t")



