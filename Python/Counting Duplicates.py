# Counting duplicates

# Basic method

def duplicate_count(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)

# Clever method

def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

# Using a module

from collections import Counter

def duplicate_count(text):
    return sum(1 for c, n in Counter(text.lower()).iteritems() if n > 1)