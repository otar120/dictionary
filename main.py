f = open("history.txt","r")
f1 = open("history.txt","r")
word = input("word: ")
len = input("which len is it? eng/ger: ")
b = ""
s = f.readline().replace("\n","")
s = int(s)
guess_word = True
i = 1
while i <= s and len == "eng":
  a = f.readline().replace("\n","")
  c,d = a.replace("-"," ").split(" ")
  if word == c:
    b = d
    break
  i += 1
while i <= s and len == "ger":
  a = f.readline().replace("\n","")
  c,d = a.replace("-"," ").split(" ")
  if word == d:
    b = c
    break
  i += 1

print(b)
f.close()
f1.close()