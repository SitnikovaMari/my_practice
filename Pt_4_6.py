def rot13(phrase):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   new_phrase = ""
   for char in phrase:
       new_phrase += alphabet[(alphabet.find(char)+13) % 26]
   return new_phrase
phrase = input("Введите строку на английском: ")
print("Закодированная строка: ", rot13(phrase))