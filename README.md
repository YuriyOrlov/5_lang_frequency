# Frequency Analysis of Words

This script takes your file and counts words in it.
Then it gives back to you list with the thirty most frequent words in the text in descending order.

It works with CP1251 encoding, because there was some problems with UTF-8 coding in some texts on Russian language.


### Usage example

Example of script launch on Linux, Python 3.5:

I used text file with Shakespeare sonnets from here:
https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt

```#!bash

$ python lang_frequency.py <path to file>
The thirty most frequent words in the text (in descending order)
1. the
2. I
3. and
4. to
5. of
6. a
7. you
8. my
9. in
10. is
11. that
12. not
13. me
14. And
15. with
16. it
17. be
18. his
19. your
20. for
21. this
22. have
23. him
24. he
25. thou
26. will
27. as
28. so
29. The
30. but

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
