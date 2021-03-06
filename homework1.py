import itertools

def list_from_dictionary(filename):
        # 辞書ファイルをリストにする
        # 辞書の単語を小文字にする
        # 辞書の単語に qu が現れたら q に置換する
        # dic_list = [line.strip().lower().replace("qu", "q") for line in open(filename)]
        # return dic_list

        dic_list = list()
        for line in open(filename, "r"):
                word = line.strip().lower().replace('qu', 'q')
                point = calc_point(word)
                length = len(word)
                dic_list.append((word, point, length))
        
        return sorted(dic_list, key = lambda x: (-x[1], -x[2]))

def calc_point(word):
        # 単語の点数を計算して点数を返す
        dict_point = {"a":1, "b":1, "d":1, "e":1, "g":1, "i":1, 
                        "n":1, "o":1, "r":1, "s":1, "t":1, "u":1, 
                        "c":2, "f":2, "h":2, "l":2, "m":2, "p":2,
                        "v":2, "w":2, "y":2, 
                        "j":3, "k":3, "q":3, "x":3, "z":3}
        
        point = 0
        for i in range(len(word)):
                point += dict_point[word[i]]
        
        point = (point + 1) ** 2
        return point


if __name__ == "__main__":
        ## [1] 与えられた文字が全て入っているプログラム
        ## 与えられた文字列をソートしたものを、ソートした全ての辞書の単語と比べる

        dic_list = list_from_dictionary("dictionary.words")
        
        while True:
                print("Please enter '0' if you want to quit")
                print("Please enter 'Q' or 'q' for 'Qu'")


                # 入力された文字列を受け取る
                str1 = input(">> ")

                if str1 == "0":
                        break

                # 入力された文字列をソートする
                # 入力された文字列を小文字にする
                sorted_str1 = sorted(str1.lower())

                #for word in dic_list:
                        #if sorted_str1 == sorted(word):
                                #print("word = ", word)

                ## [2] 与えられた文字の一部しか入っていない単語も見つけられるプログラム

                list_of_sets_of_substrings = [set() for i in range(len(str1))]  # 文字数分の入れ物を作る
                for i in range(len(sorted_str1)):
                        sub_list = [''.join(l) for l in itertools.combinations(sorted_str1, i+1)] # 文字数ごとにsubstringsのlistを作る
                        sub_set = set(sub_list) # setに代入して重複をとりのぞく
                        list_of_sets_of_substrings[i] = sub_set  # i 番目の配列要素を書き換える

                # max_point = 0
                # max_word = ""
                for (word, point, length) in dic_list:
                        if len(word) > len(str1): # 与えられた文字の文字数より辞書の単語の文字数が多かったら排除
                                continue
                        if not ''.join(sorted(word)) in list_of_sets_of_substrings[len(word) - 1]: # 同じ文字数で比較する
                                continue
                                        
                        print("*** best anagram ***")
                        print(word, " = ", point)
                        break


        print("bye")