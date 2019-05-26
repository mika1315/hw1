# 辞書の単語を読み込んでリストにする
filename = "dictionary.words"
dic_list = [line.strip() for line in open(filename)]

# 入力された文字列を受け取る
# 入力された文字列をソートする
words = input(">> ")
sorted_words = sorted(words.lower())

for word in dic_list:
    if sorted_words == sorted(word):
        print("word = ", word)