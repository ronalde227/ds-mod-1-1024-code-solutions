# -*- coding: utf-8 -*-
"""letters_to_symbols.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oVH4cKQI-Q_bYc6WbBNvd9OGcX93FjAu

#Exercise 5
"""

def letters_to_symbols(text):
  if len(text) == 0:
    return
  symbol_text = ""
  current_char = text[0]
  counter = 0

  for index in range(len(text)):
    if current_char == text[index]:
      counter += 1

      print("Entered first if statement 1:" + symbol_text)
      if(index == len(text)-1):
        symbol_text = symbol_text+str(counter)+current_char
        print("Entered second if statement 2:" + symbol_text)
    else:
      symbol_text = symbol_text+str(counter)+current_char
      current_char = text[index]
      counter = 1
      print("Entered third if statement 3:" + symbol_text)
      print(current_char)
      print(counter)
      if(index == len(text)-1):
        symbol_text = symbol_text+str(counter)+current_char
        print("Entered second if statement 2:" + symbol_text)

  return symbol_text

s="ABBBc"

letters_to_symbols(s)