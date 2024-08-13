# Jounal Entry Retrieval 
A program that looks at a database of journal entries and uses a key word to pull journal entries matching this keyword.
Built for LING508 in the Univeristy of Arizona HLT program.

## What does this application do?
Using a prepopulated database, this application is able to call upon an author of a journal and return the journals 
associated with that journal. Various strategies were used to keep the program scalable, like keeping the SQL database
separate from the classes for easy transition of database. There is a service layer that joins the database and classes.
There is then an API that accesses that data and returns the requested information in JSON format. 

An HTML file is used to navigate all authors or to input an author of one's choosing. 

## Use case #1
User is able to enter a keyword that returns journal entries containing the keyword
- _Input:_ User inputs several text data entry
- _Output:_ Program returns keywords used from the text data entries

#### See `API.md` for information on how to run app