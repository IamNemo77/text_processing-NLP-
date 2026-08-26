#import libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#library for the available items and shelf they can be found
inventory = {
    "apples" : "Shelf 1",
    "apple" : "Shelf 1",
    "milk" : "shelf 3",
    "detergent" : "shelf 5",
    "bananas" : "shelf 1",
    "banana" : "shelf 1",
    "onions" : "shelf 2",
    "onion" : "shelf 2",
    "garlic" : "shelf 2",
    "spinach" : "shelf 2",
    "potatoes" : "shelf 2",
    "potato" : "shelf 2",
    "tomatoes" : "shelf 2",
    "tomato" : "shelf 2",
    "eggs" : "shelf 4",
    "egg" : "shelf 4",
    "butter" : "shelf 3",
    "yogurt" : "shelf 3",
    "yogurts" : "shelf 3",
    "cheese" : "shelf 3",
    "chicken" : "shelf 4",
    "beef" : "shelf 4",
    "fish" : "shelf 4",
    "rice" : "shelf 6",
    "pasta" : "shelf 6",
    "beans" : "shelf 6",
    "bread" : "shelf 6",
    "oats" : "shelf 6",
    "tea" : "shelf 7",
    "coffee" : "shelf 7",
    "chocolate" : "shelf 7",
    "chocolates" : "shelf 7",
    "soap" : "shelf 5",
    "soaps" : "shelf 5",
    "shampoo" : "shelf 5",
    "towel" : "shelf 5",
    "towels" : "shelf 5"
}

#taking an input from the user
items = input ("Hi! I'm SNUBOT. \nI can help you to see where the items you want can be found. \nWhat are you going to buy today?\n")

#tokenizing the words 
words = word_tokenize(items)
tagged_words = pos_tag(words)

#identifying the items the user is looking for
nouns = [word for word, tag in tagged_words if tag.startswith('NN')]

#display items and the shelfs they can be found
for item in nouns:
    #convert entered the items into lower case
    clean_item = item.lower()
    if clean_item in inventory:
        print(f"{clean_item} --> {inventory[clean_item]}")