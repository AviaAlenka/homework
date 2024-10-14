
def single_root_words_1(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if root_word.lower() in other_words[i].lower():
            same_words.append(other_words[i])
    print(same_words)

def single_root_words_2(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if other_words[i].lower() in root_word.lower():
            same_words.append(other_words[i])
    print(same_words)

print("Проверим, в какие слова неограниченной последовательности входит обязательное слово")
root_word = str(input("Введите обязательное слово: "))
other_words = list(input("Введите произвольную последовательность: ").split())
single_root_words_1(root_word, *other_words)

# single_root_words_1('rich', 'richiest', 'orichalcum', 'cheers', 'richies') - исходный вариант вызова функции до заморачивания со вводом с клавиатуры :-)

print("Проверим, какие слова из неограниченной последовательности содержит обязательное слово")
root_word = str(input("Введите обязательное слово: "))
other_words = list(input("Введите произвольную последовательность: ").split())
single_root_words_2(root_word, *other_words)

# single_root_words_2('Disablement', 'Able', 'Mable', 'Disable', 'Bagel') - исходный вариант вызова функции до заморачивания со вводом с клавиатуры :-)

