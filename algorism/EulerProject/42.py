words = ""
with open("./data/words.txt", "r") as f:
    words = f.readline()
words = [sum([ord(j) - 64 for j in i.replace("\"", "")]) for i in words.split(",")]

print(words)

triNumbers = []
temp, count = 0, 0
while temp < max(words):
    temp = count*(count+1)//2
    triNumbers.append(temp)
    count += 1
print(triNumbers)

count = 0
for i in words:
    if i in triNumbers:
        count += 1

print(count)
