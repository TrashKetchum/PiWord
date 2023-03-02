with open('allwords.txt') as f:
    words = f.readlines()
    f.close()

with open('pi_letters') as a:
    lines = a.readlines()
    a.close()

pi = ""
for line in lines:
    for letter in line:
        pi += letter
long = ""
longer = []
for word in words:
    word = word.replace("\n", "")
    if len(word)>len(long):
        if word in pi:
            long = word

for word in words:
    word = word.replace("\n", "")
    if len(word)==len(long):
        if word in pi:
            longer.append(word)

for i in longer:
    print(i)