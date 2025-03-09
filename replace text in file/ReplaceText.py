def replaceText(inFile, outFile, old_word, replace_word):
    '''
    replace word in file with a new word
    :param inFile: input text file
    :param outFile: output text file
    :param old: the word been searched
    :param new: the word to be replaced
    :return:
    '''

    reader = open(inFile, mode="r", encoding="UTF-8")
    writer = open(outFile, mode="w", encoding="UTF-8")

    text = reader.readlines()

    for line in text:
        newLine = line.replace(old_word, replace_word)
        writer.write(newLine)

    reader.close()
    writer.close()

# def replaceText(old_string, old_word, new_word):
#     '''
#     replace word in a string with a new string
#     :param old_string: input string
#     :param old_word: the word been searched
#     :param new_word: the word to be replaced
#     :return: output string
#     '''
#     return old_string.replace(old_word, new_word)

if __name__ == "__main__":

    inFile = "data.txt"
    outFile = "result.txt"
    old_word = "World"
    new_word = "Python"

    replaceText(inFile, outFile, old_word, new_word)