with open('pi.txt') as f:
    lines = f.readlines()
    f.close()
pi = ""
hold = 0
phrase = "thomas"
check = ""
count = 0
for line in lines:
    for digit in line:
        pi += digit
for i in range(0, len(pi)-1):
    if i % 2 == 0:
        hold = int(pi[i:i+2]) % 26
        check += chr(hold+97)
    if len(check) >= len(phrase):
        if check == phrase:
            print(str(i-((len(check)-1)*2)+1)+" | "+str(i+2))
            check=""
            count+=1
        else:
            check = check[1:]

print(count)
