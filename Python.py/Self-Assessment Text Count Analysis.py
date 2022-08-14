Step 1: Normalize the Letter Casing
s = """Imagine a vast sheet of paper on which straight Lines, Triangles, Squares, Pentagons, Hexagons, and other figures, instead of remaining fixed in their places, move freely about, on or in the surface, but without the power of rising above or sinking below it, very much like shadows - only hard and with luminous edges - and you will then have a pretty correct notion of my country and countrymen. Alas, a few years ago, I should have said "my universe": but now my mind has been opened to higher views of things."""
 
    #do not change any code above this line
    #your code here
sl=s.lower()

Step 2: Split the String into Words
words = list() #do not delete. this list must contain the list of words. 
 
#your code goes here
words=sl.split() 
print(words) #do not delete 
#do not write any code past here

Step 3: Count the Words
len(words)

Step 4: Count the Distinct Words
len(set(words))

Step 5: Compute the Word Frequencies
freq_occur = dict()
for word in words:
    if word in freq_occur.keys():
       freq_occur[word]+=1
    else:
       freq_occur[word]=1
       
Step 6: Remove Punctuation Marks
 import string #import the string module 
    #use the built-in string.punctuation method to create a list of all punctuation marks
    punctuation_list =  list(string.punctuation)

    print(words)
    w_clean = list() 

 
    #your code goes here 
    for i in words:
      for j in i:  
        if j in punctuation_list:
          i=i.replace(j,'')
          print(i) 
      if len(i)>1:
        w_clean.append(i)
        
    
 
    print(w_clean)
    print(len(w_clean))
    
Step 7
Finally, create a single script that performs all of the following operations on the original 's' string.

Convert the string to lowercase characters.
Split the lowercase string into individual words.
Remove the punctuation from the lowercase words. Assume that all punctuation is either the first character or the last character of each item in the list.
Perform a count analysis on the words without punctuation characters.
Display the dictionary with the word counts and the number of distinct words in the original string.

s = """Imagine a vast sheet of paper on which straight Lines, Triangles, Squares, Pentagons, Hexagons, and other figures, instead of remaining fixed in their places, move freely about, on or in the surface, but without the power of rising above or sinking below it, very much like shadows - only hard and with luminous edges - and you will then have a pretty correct notion of my country and countrymen. Alas, a few years ago, I should have said "my universe": but now my mind has been opened to higher views of things."""
sl=s.lower()
words = list()  
words=sl.split()     
import string #import the string module 
punctuation_list =  list(string.punctuation)  
w_clean = list() 
for i in words:
  for j in i:  
    if j in punctuation_list:
      i=i.replace(j,'') 
  if len(i)>1:
      w_clean.append(i)
freq_occur = dict()
for word in w_clean:
    if word in freq_occur.keys():
       freq_occur[word]+=1
    else:
       freq_occur[word]=1    
print(f"The word count for each word is as follows: {freq_occur}\nThe number of distinct words in the original string is: {len(set(words))}") 
