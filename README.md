# Introduction

TypeNwrite has been made to immitate handwriting of a person to help him/her write scripts in his/her own handwriting.
All the user needs to do it provide the program the images of alphabets written by the user and the program will be ready to work.
Just provide the typed text you want to be written in you handwriting and the program will output and image of text written in your hand writing.

# How to use?

First make sure your computer has the following in it :
1. Python3
2. Required python3 libraries, namely PIL(pillow) and Tkinter

## Note for windows users: 
Make sure python3 shows up in command prompt.

## Creating handwriting profile:
To create a new profile go through the following steps:

1.Create an empty folder(its name is up to you but in this guide I'll call it "source folder").

2.Take snapshots of each alphabet separately. Make sure the text has been written on a clean white page(with no lines in it) and with a black colored pen.

3.Name each image according to the following format-

XTG.jpg or XTG.png
  
Here,

X = the alphabet the image has in it.

T = a number between 1 to 4 which denotes type of alphabet (it is explained in the images below)

G = any string of letter(completely optional, added just in case the computer has problem in naming the image)
  
G can be an empty string, so XT.jpg and XT.png are also valid formats
  
![lines](https://github.com/AnuragS13/TypeNwrite/blob/main/Letter_Types.jpg)
  
Consider the above as children's alphabet writing notebook
If your letter -
Has line 1 as top and line 3 as bottom then it is of type 1.

Has line 2 as top and line 3 as bottom then it is of type 2.

Has line 2 as top and line 4 as bottom then it is of type 3.

Has line 1 as top and line 4 as bottom then it is of type 4.
  
  
## Adding handwriting profile:
1. Run gui.py file.
2. Open menu.
3. Click on create new profile.
4. Enter profile name and the name of the folder which contains the snapshots.
5. Click on create.

## How to write?
1. Run gui.py
2. Enter you text in input
3. Select writing profile
4. Click on get copy

Note : The output will be in the same folder with the name "test_sample.jpg".

# Developer's Note:

TypeNwrite is not complete yet. I'll keep adding new things when I get time and new ideas.
Feel free to suggest improvements.
Peace!
