import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = dict()
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                list_words = []
                for line in file.readlines():
                    for word in line.split():
                        word = word.translate(str.maketrans('', '', string.punctuation)).lower()
                        list_words.append(word)
                all_words[file_name] = list_words
        return all_words

    def find(self, word):
        all_find = dict()
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                all_find[name] = words.index(word) + 1
        return all_find

    def count(self, word):
        all_count = dict()
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                all_count[name] = words.count(word)
        return all_count


finder = WordsFinder('test1.txt', 'test2.txt', 'test3.txt')
print(finder.get_all_words())
print(finder.find('text'))
print(finder.count('text'))
