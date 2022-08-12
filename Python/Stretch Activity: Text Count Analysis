Once you have completed the script for this module's assignment and 
the script works as expected to count distinct words in a string, try the following stretch activities:

Set up the script to allow the user to enter their own text at runtime and perform the operations on the user input.
Prompt the user for a word and return that word's frequency in a selected string.
Sort the items in the dictionary alphabetically.
Sort the items in the dictionary from the highest frequency to the lowest frequency (or vice versa).
You may need to search for examples on how to perform these activities in Python.

word=input("Please input a text paragraph to analyse: ")
w=input("Input a word to check its frequency: ")
words=word.split()
freq_occur={}
for i in words:
    if i in freq_occur.keys():
       freq_occur[i.lower()]+=1
    else:
       freq_occur[i.lower()]=1   
print(f"The frequency of the word {w} is {freq_occur[w]}")       
alphasort=sorted(freq_occur.items())
print(f"Sorted alphabetically: {alphasort}")
freqsort=sorted(freq_occur.items(), key=lambda x: x[1], reverse=True)
print(f"Sorted by frequency: {freqsort}")

       
