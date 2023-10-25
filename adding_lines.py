with open("path_to_file/file.txt", "r") as f:               #file to manipulate
    contents = f.readlines()

word = "word"

word_lines = open("path_to_file/file_with_word.txt", "r")   #file that contains the lines we are interested in    
for count, i in enumerate(word_lines):
    if i.startswith(word):                                  #can be changed with other options (e.g. i.find(word))
        contents.insert(count, i)

with open("path_to_file/file_new.txt", "w") as f:           #new file with added lines in specific index locations
    contents = "".join(contents)
    f.write(contents)
