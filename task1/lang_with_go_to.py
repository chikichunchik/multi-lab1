from goto import with_goto

@with_goto
def find(mass, value, size):
    pointer = 0
    label.loop
    if mass[pointer] == value:
        return pointer
    pointer += 1
    if pointer == size:
        return -1
    goto.loop

@with_goto
def word_count(file):
    word_counter = 0
    label.loop
    input_symbol = file.read(1)
    if not input_symbol:
        file.close()
        return word_counter + 1
    elif input_symbol == ' ' or input_symbol == '\n':
        word_counter += 1
    goto.loop

@with_goto
def every_word_count(file, word_number):
    buzzwords = ['the', 'for', 'in']
    buzzwords_size = 3
    high_alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low_alfabet = 'abcdefghijklmnopqrstuvwxyz'
    words = ['']*word_number
    words_count = [0]*word_number
    current_word = ''
    pointer = 0
    label.loop
    input_symbol = file.read(1)
    if not input_symbol:
        file.close()
        goto.end
    if input_symbol != ' ' and input_symbol != '\n':
        find_symbol = find(high_alfabet, input_symbol, 26)
        if find_symbol != -1:
            input_symbol = low_alfabet[find_symbol]
        current_word += input_symbol
    else:
        if find(buzzwords, current_word, buzzwords_size) != -1:
            current_word = ''
            goto.loop
        find_result = find(words, current_word, word_number)
        if find_result == -1:
            words[pointer] = current_word
            words_count[pointer] = 1
            pointer += 1
        else:
            words_count[find_result] += 1
        current_word = ''
    goto.loop
    label.end
    if find(buzzwords, current_word, buzzwords_size) != -1:
        return words_count, words
    find_result = find(words, current_word, word_number)
    if find_result == -1:
        words[pointer] = current_word
        words_count[pointer] = 1
        pointer += 1
    else:
        words_count[find_result] += 1
    file.close()
    return words_count, words

@with_goto
def sorting(list1, list2, size):
    i = 0
    j = 0
    label.loop1
    label.loop2
    if list1[j] < list1[j + 1]:
        list1[j], list1[j + 1] = list1[j + 1], list1[j]
        list2[j], list2[j + 1] = list2[j + 1], list2[j]
    if j + 1 != size - 1 - i:
        j += 1
        goto.loop2
    else:
        j = 0
    if i + 1 != size - 1:
        i += 1
        goto.loop1
    else:
        return list1, list2

@with_goto
def print_result(words_count, words, size):
    pointer = 0
    label.printloop
    if pointer == size or words_count[pointer] == 0:
        return
    print(words[pointer] + ' - ' + str(words_count[pointer]))
    pointer += 1
    goto.printloop


input_file = open('task1/text.txt', 'r')
word_number = word_count(input_file)
input_file = open('task1/text.txt', 'r')

print_result(*sorting(*every_word_count(input_file, word_number), word_number), word_number)

