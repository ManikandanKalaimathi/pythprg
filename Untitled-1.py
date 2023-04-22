hefrom collections import Counter
def scramble(str1, str2):
    if str1 is None or str2 is None:
        return False
    if len(str1) < len(str2):
        return False
    c1 = Counter(str1)
    c2 = Counter(str2)
    for char, count in c2.items():
        if char not in c1 or c1[char] < count:
            return False
        
    return True

str1 = input()
str2 = input()
print(scramble(str1, str2))