# Frequency Analysis of Words

This script takes your file and counts words in it. Furthermore, it could delete stopwords from russian language. Words corpus for this function were taken from **nltk** library.
After work this script will provide you with a list of ten most frequent words in the text in descending order. 

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
