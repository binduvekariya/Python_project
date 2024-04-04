# pip install PyDictionary
# from PyDictionary import PyDictionary

# dictionary = PyDictionary()
# dictionary.meaning("eyes")

# dict = PyDictionary("eyes", "indentation", "head")
# print(dict.printmeaning())
# print(dict.getmeaning())   -> if we use get method the output in form of dictionary






def main():
    word_dict  = {
        "hi" : "A way of greeting",
        "eyes" : "An organ for seeing",
        "earth" : "A planet in space",
    }

    while True:
        word = input("Enter a word: ")
        if word == " ":
            break
        if word in word_dict:
            print(word, ": ",word_dict[word])


main()
