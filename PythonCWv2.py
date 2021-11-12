# function to find the longest
# length in the list
def get_longest_word(list_of_words):
    max1 = len(list_of_words[0])
    temp = list_of_words[0]

    # for loop to traverse the list
    for i in list_of_words:
        if (len(i) > max1):
            max1 = len(i)
            temp = i

    print("The word with the longest length is:", temp,
          " and length is ", max1)


# Driver Program
list_of_words = ["one", "two", "third", "four"]
get_longest_word(list_of_words)