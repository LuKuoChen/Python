#如何使用字串、字串的用法
print("Hello Mr.Lu")
print("Hello \nMr.Lu")
print("\"Hello\" Mr.Lu")
print("Hello"+" "+"Mr.Lu")

phrase="Hello"
name="Mr.Lu"
print(phrase+" "+name)

#函式 function
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print(phrase.lower().islower())
print(phrase.lower().isupper())
print(phrase[1])
print(phrase.index("H"))
print(phrase.replace("H","h"))