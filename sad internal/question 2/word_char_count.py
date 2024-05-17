def word_char_count(sentense):
    word_count=len(sentense.split())
    char_count=len(sentense.replace(" ",""))
    return word_count , char_count
sentense="hello iam umesh and iam from aditya college of engineering"
word_count,char_count=word_char_count(sentense)
print("All the characters in string is :",char_count)
print("All the words in string is :",word_count)