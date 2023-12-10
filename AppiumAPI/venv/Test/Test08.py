##items=[x for x in input().split(',')]
##items.sort()
freq={}
print('请输入：')
line=input()
for word in line.split():
    freq[word]=freq.get(word,0)+1
    print(freq[word])
words=sorted(freq.keys())
