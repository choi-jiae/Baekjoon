def hash(chars):
    result = 0
    r = 31
    M = 1234567891
    for i, c in enumerate(chars):
        result += (ord(c)-ord('a')+1)*r**i
    
    return result%M

L = int(input())
chars = input()
print(hash(chars))