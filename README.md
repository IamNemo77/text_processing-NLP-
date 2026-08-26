SNUBOT is a lightweight, conversational Python script designed to help users quickly locate items in a grocery store. By leveraging basic Natural Language Processing (NLP), SNUBOT parses a user's typed sentence, extracts the names of the grocery items, and matches them against an internal shelf inventory database.

Features

Conversational Input : Accepts full sentences from users (ex : "I need to buy some milk, eggs, and an apple").
NLP Tokenization : Automatically parses sentences using NLTK.
Smart Item Extraction : Filters out filler words, focusing specifically on nouns (grocery items).
Instant Shelf Mapping : Maps identified items directly to their corresponding store shelves.

Prerequisites

Before running SNUBOT, you need to install Python 3 and the `nltk` library.

How to Run

1.  Clone or download the script file to your local computer.
2.  Open your terminal or command prompt and run the script.
3.  Interact with SNUBOT when prompted

Example Input

> "Hi! I'm SNUBOT. 
> I can help you to see where the items you want can be found. 
> What are you going to buy today?"
> 
> User: "I want to buy milk, apples, and some tea."

Example Output

milk --> shelf 3
apples --> Shelf 1
tea --> shelf 7

Core Architecture

The script uses a step-by-step pipeline to handle user inputs:
1.  Dictionary Lookup : Houses a pre-defined `inventory` dictionary mapping singular and plural items to specific shelves.
2.  Tokenization : Breaks down user text into individual words using NLTK's `word_tokenize`.
3.  POS Tagging : Assigns grammatical tags using `pos_tag` to isolate words tagged as nouns (NN).
4.  Case Normalization : Converts extracted nouns to lowercase to prevent dictionary matching issues due to uppercase letters."# customer-care-chatbot" 
