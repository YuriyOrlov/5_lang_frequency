# Frequency Analysis of Words

This script takes your file and counts words in it. Program detects your language to choose the list of stop-words according to your language. If this is impossible it goes further without using that list. This has been made with the help of  **nltk** library, so it also needed to be installed and all word corpuses have to be dowloaded.
Then it gives back to you list with the ten most frequent words in the text in descending order. 

How to install **nltk** library with words corpus:

```#!bash
$pip install -r requirements.txt && python

```
When **nltk** library will has installed and you are in python interpreter:

```
>>> import nltk
>>> nltk.download('all')

```
ATTENTION: Please, don't try to use GUI interface for package downloading, because it could cause mistakes.

More information about this problem can be found here:
http://stackoverflow.com/questions/33183618/nltk-data-out-of-date-python-3-4

### Usage example

Example of script launch on Linux, Python 3.5:

I used text file with Shakespeare sonnets from here:
https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt

```#!bash

$ python lang_frequency.py <path to file> <number of words to show in result>

The ten most frequent words in the text (in descending order)
1. thou
2. thy
3. shall
4. thee
5. lord
6. king
7. good
8. sir
9. come
10. well

```
I've tested this script on Russian, English, French, Chineese and Esperanto languages and program works well.
Other tests are welcome!

More texts on different languages here:
http://www.gutenberg.org/

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
