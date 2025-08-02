def count_words(path):
    with open(path) as f:
        count = len(f.read().split())
        return count


def count_chars(path):
    with open(path) as f:
        count = {}
        for c in f.read():
            if c.lower() in count:
                count[c.lower()] += 1
            else:
                count[c.lower()] = 1
        return count

def report(path):
    counts = count_chars(path)
    counts_list = [(k, counts[k]) for k in counts]
    f_cmp = lambda x: x[1]
    counts_list.sort(key=f_cmp,reverse=True)
    word_count = count_words(path)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n----------- Word Count ----------\nFound {word_count} total words\n--------- Character Count -------")
    for e in counts_list:
        if e[0].isalpha():
            print(f"{e[0]}: {e[1]}")
    print("============= END ===============")
