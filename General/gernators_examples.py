from General.iterators_example import FileIterator


def vowel_generator():
    yield 'a'
    yield 'e'
    yield 'i'
    yield 'o'
    yield 'u'


def file_search(file_name, keyword):
    fi = FileIterator(file_name)
    for line in fi:
        if keyword in line:
            yield line


def main():
    # A simple sequence generator
    sq = (x * x for x in range(5))
    print(sq)
    for s in sq:
        print(s)

    # Vowel letters generator
    vg = vowel_generator()
    print(vg)
    for v in vg:
        print(v)

    # A file search generator
    fg = file_search('input.txt', 'purpose')
    print(fg)
    for line in fg:
        print(line)


if __name__ == '__main__':
    main()