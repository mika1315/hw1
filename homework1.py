import itertools

def list_from_dictionary(filename):
        # 辞書ファイルをリストにする
        dic_list = [line.strip() for line in open(filename)]
        return dic_list

## [1] 与えられた文字が全て入っているプログラム
## 与えられた文字列をソートしたものを、ソートした全ての辞書の単語と比べる

# 入力された文字列を受け取る
str1 = input(">> ")

# 入力された文字列をソートする
sorted_str1 = sorted(str1.lower())

dic_list = list_from_dictionary("dictionary.words")
for word in dic_list:
        if sorted_str1 == sorted(word):
                print("word = ", word)

## [2] 与えられた文字の一部しか入っていない単語も見つけられるプログラム

list_of_sets_of_substrings = [set() for i in range(len(str1))]  # 文字数分の入れ物を作る
for i in range(len(sorted_str1)):
        sub_list = [''.join(l) for l in itertools.combinations(sorted_str1, i+1)]
        sub_set = set(sub_list)
        list_of_sets_of_substrings[i] = sub_set  # i 番目の配列要素を書き換える

for word in dic_list:
        if len(word) <= len(str1):
                if ''.join(sorted(word.lower())) in list_of_sets_of_substrings[len(word) - 1]:
                        print("word = ", word)