with open("file.txt","r") as file:
    word_count=0
    for line in file:
        word_count+=len(line.split())
    print(word_count)