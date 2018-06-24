class FileIterator:
    def __init__(self, file_name):
        self.__fh = open(file_name)
        self.__lines = self.__fh.readlines()
        self.__idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.__idx += 1
            return self.__lines[self.__idx]
        except IndexError:
            raise StopIteration()


def main():
    fi = FileIterator('input.txt')
    for line in fi:
        print(line)


if __name__ == '__main__':
    main()
