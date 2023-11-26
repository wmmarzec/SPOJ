import sys
try:

    n = input()
    for i in range (0, int(n)):
        words = input().split()
        word_to_check = words[0]
        wanted_word = words[1]
        target_index = 0
        new_word = ""

        for j in range (0, len(word_to_check)):
            if word_to_check[j] == wanted_word[target_index]:
                new_word += wanted_word[target_index]
                target_index += 1
                if new_word == wanted_word:
                    break

        if new_word == wanted_word:
            print ("Tak")
        else:
            print ("Nie")

except:
    sys.exit(0)