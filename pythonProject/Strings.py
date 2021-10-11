""" 20 Exercise

name = str(input("Enter the Name: "))
lenght = len(name)
print(lenght)

"""
""" 21 Exercise 
firstname = str(input("Enter your Name: "))
surname = str(input("Enter your Surname: "))
fs = firstname + " " + surname
lenght = len(fs)
print(fs, lenght)
"""

""" 22 Exercise
firstname = str(input("Enter your Name if lowercase: "))
surname = str(input("Enter your Surname in lowercase: "))
firstname = firstname.title()
surname = surname.title()
final = firstname + " " + surname
print(final)
"""

""" 23 Execise
text1 = str(input("Enter text: "))
lenght = len(text1)
print("Lenght line - ", lenght)
start = int(input("Enter start number:"))
end = int(input("Enter end number: "))
print(text1[start:end])
"""
""" 24 Execise
name1 = str(input("Enter your Name - "))
name1 = name1.upper()
print(name1)
"""

""" 25 Execise
name1 = str(input("Enter your Name - "))
lenght = len(name1)
if lenght < 5:
    surname = str(input("Enter your Surname -"))
    final = name1 + surname
    final = final.upper()
    print(final)
else:
    name1 = name1.lower()
    print(name1)
"""

""" 26 Execise
word = str(input("Enter word - "))
first = word[0]
length = len(word)
rest = word[1:length]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u" and first != "y":
    newword = rest + first + "ay"
else:
    newword = word + "way"
print(newword.lower())
"""