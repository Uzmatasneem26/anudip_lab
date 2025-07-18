#read content forrm the text file and display the same
file= open("abc.txt","w")
file.write("this is a pyhton learning class")
file.close()

with open ("abc.txt","r")as file:
    a=file.read()
    print(a)

#count the number of words in a file
with open ("abc.txt","r")as file:
    contents=file.read()
    words=contents.split()
    word_count=len(words)
    print(f"the total number of words in a file is :{word_count}")


#count the number of uppercase letters in a file
with open("abc.txt","r") as file:
    contents=file.read()
    words=contents.split()
    count=0
    for i in words:
        if i.isupper():
            count+=1
    print("the total number of capital letters are: ",count)


# Write a function display_words() in python to read lines from a text file "story.txt",
def display_words():
    with open("abc.txt","r") as file:
        a=file.read()
        words = a.split()
        print("words with less than 4 characters:") 
        for word in words :
            if len(word)<4:
                print(word)
        return len(words)
    
print("the total number of words in the file is :",display_words())
