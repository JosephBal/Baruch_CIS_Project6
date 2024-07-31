# Baruch_CIS_Project6
This was my 7th project in my CIS 2300 "Programming and Computational Thinking" led by professor Sadat Chowdhury

# Project Description

Design a function as follows:

mc(symbol)

The function should *return* the appropriate morse code for the given symbol according to the table for International Morse Code listed here: https://en.wikipedia.org/wiki/Morse_code

For e.g., 

```
mc('a') should return '.-'

mc('A') should return '.-'

mc('k') should return '-.-'

mc('1') should return '.---'

mc(1) should return '.---'
```
Notice, how the function is able to handle both lower and upper case forms of letters. It is also able to handle both the string and int forms of a given numeric symbol.

If the symbol is not recognized, the function should return None

Once you have designed the function, in the main body of your program, write code that uses your function and displays, in a single line of output, the morse code for your 7 letter word and 5 digit number. Each morse code for the letters should be separated by a single space. 

As an e.g., my word is orchids and number is 12345, so I will output the translation for orchids12345. That output should be: 
```
--- .-. -.-. .... .. -.. ... .---- ..--- ...-- ....- .....
```
