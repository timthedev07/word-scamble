from wsfinder import main

finder = main.Finder("english")
scrambled_words = [
    "taurdesta",
    "achwt",
    "ilane",
    "alger",
    ]

res = {word:finder.find(word) for word in scrambled_words}
print(res)