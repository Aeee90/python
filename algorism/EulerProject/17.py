def getCount(arr):
    count = 0
    for i in arr:
        count += len(i)
    return count

oneCiphers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
twoCiphers1 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
twoCiphers2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
threeCiphers = ['hundred']
fourCiphers = ['onethousand']

oneCiphersCount = getCount(oneCiphers)
twoCiphersCount1 = getCount(twoCiphers1)
twoCiphersCount2 = getCount(twoCiphers2)
threeCiphersCount = getCount(threeCiphers)
fourCiphersCount = getCount(fourCiphers)
andCount = 3

num = 1000
result = 0
#1의 자리
result += oneCiphersCount*9*10
#10의 자리
result += twoCiphersCount1*10
result += twoCiphersCount2*10*10
#100의 자리
result += oneCiphersCount + threeCiphersCount*9 + (oneCiphersCount + threeCiphersCount*9 + andCount*9)*(100-1)
#1000의 자리
result += fourCiphersCount

print(result)


words1000 = 'thousand'
words100 = 'hundred'
words20 = ('', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
           'seventy', 'eighty', 'ninety')
words1 = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
          'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
          'sixteen', 'seventeen', 'eighteen', 'nineteen')

def words(n):
    s = ""
    if n == 1000:
        s += words1[n // 1000] + words1000
        n = n % 1000
    if n > 99:
        s += words1[n // 100] + words100
        n = n % 100
        if n > 0:
            s += "and"
    if n >= 20:
        s += words20[n // 10]
        n = n % 10
    s += words1[n]
    return s

def p17():
    print(sum([len(words(n)) for n in range(1, 1001)]))

p17()