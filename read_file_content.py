file=open("sample.txt","r")

line_count=0
word_count=0

for line in file:
    line_count+=1
    words=line.split()
    word_count+=len(words)

file.close()

print("Number of lines:",line_count)
print("Number of words:",word_count)
