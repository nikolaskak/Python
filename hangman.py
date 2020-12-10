myWord = []
word = input("Give a word: \t")
m= len(word)
print(m)
myWord.append(word)
i = 5
while i >=0:
    j = input("Letter: ")
    if j in word:
        print("OK")
    else:
        print("Try again!")
    
    i= i-1
   
