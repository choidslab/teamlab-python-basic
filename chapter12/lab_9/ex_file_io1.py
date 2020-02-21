
# f = open('i_have_a_dream.txt', 'w')
# f.close()

with open('i_have_a_dream.txt', 'r') as my_file:
    contents = my_file.read().strip().replace('\n', '')
    word_list = contents.split(" ")
    line_list = contents.split("\n")

    print("Total Number of Characters: ", len(contents))
    print("Total Number of Words: ", len(sorted(list(set(word_list)))))
    print("Total Number of Lines: ", len(line_list))

    print(sorted(list(set(word_list))))

