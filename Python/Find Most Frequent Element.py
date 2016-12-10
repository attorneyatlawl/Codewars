# Most Frequent Elements

def find_most_frequent(l):
    return set(x for x in set(l) if l.count(x) == max([l.count(y) for y in l]))
