#!/usr/bin/env python3
'''
	William Bowers
	Tokenizing words in Japanese text using a maxmatch algorithm
	3/18/2019
'''
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
dict_file = "japanese_wordlist.txt"


with open(dict_file,'r') as word_file:
        word_list = word_file.read().splitlines() #https://stackoverflow.com/questions/22918013/python-iterate-over-a-string-containing-newlines

with open(input_file, 'r') as in_file:
        sentences = in_file.read().split('\n') # should accomplish same thing as splitlines()
        #print(sentences)

#Use the MaxMatch Algorithm to iterate over characters in each sentence and parse them into words
'''
MAXMATCH STEPS:
- Using a dictionary, find the longest string of characters that appear in the dictionary.
- Save that string, and repeat on the remainder of the sentence.
- If a word is not encountered in the dictionary, 
  save a single character and repeat on the remainder of the sentence.
'''
spaced_line = []
def maxMatch(sentence):
    #print(sentence)
    #check if entire sentence is in the word_list
    if sentence not in word_list:
        remainder = sentence #evaluate sentence at index > 0
    while remainder not in word_list: #Paulina mentioned a while statement here would make more sense than an if statement and a for loop
        remainder = remainder[0:len(remainder)-1]
    spaced_line.append(remainder)
    remainder = remainder[len(remainder):len(sentence)] #get rest of sentence without a found word      
    print(spaced_line)
    maxMatch(remainder) #recursive
    


#Write parsed Japanese text to out_file
with open(output_file, 'w') as out_file:
    out_file.write(str())
    out_file.close()

for sentence in sentences:
    maxMatch(sentence)



