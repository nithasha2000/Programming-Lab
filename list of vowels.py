word='lovely'
print("The word is",word) #printing the word
print("List of vowels in word : ")
list=[i for i in word if (i=='a'or i=='e' or i=='i' or i=='o' or i=='u') ] #checks whether each letter in the word is vowel or not
print(list)