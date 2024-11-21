# С одним файлом всё работает (с любым словом из полученного списка).
# С "неограниченным количеством названий файлов" пока не поняла, как...

class WordsFinder:

    def __init__(self, file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}

        with open(self.file_name, encoding='utf-8') as file:
            words = file.read().lower().replace('\n', ' ')
            words = words.replace("'", "")
            words = words.replace(',', '')
            words = words.replace('.', '')
            words = words.replace('!', '').split()
            # print(words) # Проверка полученного списка
            key, value = self.file_name, words
            all_words[key] = value
        return all_words

    def find(self, word = ''):
        find = {}
        with open(self.file_name, encoding='utf-8') as file:
            words = file.read().lower().replace('\n', ' ')
            words = words.replace("'", "")
            words = words.replace(',', '')
            words = words.replace('.', '')
            words = (words.replace('!', '')).split()
            a = int(words.index(word.lower())) + 1
            key, value = self.file_name, a
            find[key] = value
            print(f"Слово '{word}' в списке - {a} по счёту")
            return find

    def count(self, word = ''):
        count = {}
        with open(self.file_name, encoding='utf-8') as file:
            words = file.read().lower().replace('\n', ' ')
            words = words.replace("'", "")
            words = words.replace(',', '')
            words = words.replace('.', '')
            words = (words.replace('!', '')).split()
            a = words.count(word.lower())
            key, value = self.file_name, a
            count[key] = value
            print(f"Слово {word} встречается в списке {a} раз")
        return count

finder2 = WordsFinder('test_file.txt' )
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего