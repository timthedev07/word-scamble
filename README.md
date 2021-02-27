# Python basic data structures implementations

**word scramble** is a python package that looks for all possibilities given a scrambled word. 



# Installation
If not already, [install pip](https://pip.pypa.io/en/stable/installing/)

Install the package with `pip` or `pip3`:

```bash
pip install word-scramble
```

# Usage

```Python
from wsfinder import main
# Need to provide the language
finder = main.Finder("english")
scrambled_words = [
    "taurdesta",
    "achwt",
    "ilane",
    "alger",
    ]
res = {word:finder.find(word) for word in scrambled_words}
print(res)
```
Output:
```Python
{
    'taurdesta': ['saturated'],
    'achwt': ['watch'],
    'ilane': ['liane', 'laine', 'elian', 'anile', 'aline', 'alien'],'alger': ['regal', 'large', 'lager', 'glare', 'elgar', 'argle'],
}
```
