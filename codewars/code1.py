import re
from itertools import product, permutations, combinations
import math
from collections import Counter

# c = 'big brown fox cought a bad rabbit'
# positive = 0
# negative = 0
# for i in c.split():
#     r = re.compile(r'^[a-m]').findall(i.lower())
#     if r:
#         positive += 1
#     else:
#         negative +=1
# if positive >= negative:
#     print(True)
# else:
#     print(False)


#
# d = 'Xylophones'
# tr = re.compile(r'^[a-m]').findall(i.lower())
# print(tr)


count = 0


def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    global count
    count += n
    return fib(n - 1) + fib(n - 2)


def permutation(string):
    return sorted({''.join(i) for i in permutations(string)})


# print(permutation('a'))

def is_square(a):
    return all(list(map(lambda x: math.sqrt(x) == int(math.sqrt(x)), a)))


def letter_only(c):
    a = re.compile(r'[A-Za-z\s]+')
    d = a.findall(c)
    print(''.join(d))


def even_or_odd(s):
    odd = sum([int(i) for i in s if int(i) % 2])
    even = sum([int(i) for i in s if int(i) % 2 == 0])
    if odd > even:
        return 'Odd is greater than Even'
    if even > odd:
        return 'Even is greater than Odd'
    if even == odd:
        return 'Even and Odd are the same'


def alphanumeric(password):
    a = re.compile(r'^[A-Za-z0-9]+$')
    if a.findall(password):
        return True
    else:
        return False


def is_nice(arr):
    if arr:
        a = [i for i in arr if i + 1 in arr or i - 1 in arr]
        if len(a) == len(arr):
            return True
        else:
            return False
    return False


class Calculator(object):
    def evaluate(self, string):
        return int(eval(string))


# s1 = re.compile(r'[a-z]+').findall("A aaaa bb c")
# s2 = re.compile(r'[a-z]+').findall("& aaa bbb c d")
# l1 = list(''.join(s1))
# l2 = list(''.join(s2))
# s1c = Counter(l1)
# s2c = Counter(l2)
# d = s1c + s2c
# print(d)
# print(s1c)
# print(s2c)
# x = []
# for i in d:
#     if s1c[i] > 1 and s2c[i] >1:
#         if s1c[i] < s2c[i]:
#             x.append(f'2:{i} {s2c[i]}')
#         elif  s1c[i] > s2c[i]:
#             x.append(f'1:{i} {s1c[i]}')
# print(x)
def f(s):
    if len(s) > 1:
        return str(s)[1:] + str(s)[0] + 'ay'
    if len(s) == 1 and s.isalpha():
        return s + 'ay'
    return s


def pig_it(text):
    return ' '.join(list(map(f, text.split())))


def digitize(n):
    return list(reversed([int(i) for i in str(n)]))


def is_same_language(lst):
    return [i['language'] for i in lst].count(lst[0]['language']) == len(lst)


list1 = [
    {'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42,
     'language': 'JavaScript'},
    {'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22,
     'language': 'JavaScript'},
    {'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 65,
     'language': 'JavaScript'},
]


#
# st = ' FIREYYFURYYFURYYFURRYFIRE'
# t = re.compile(r'(FIRE|FURY)')
# l = t.findall(st)
# c = ''
# for i in set(l):
#     if i == 'FIRE':
#         c+= f'You {"and you " * (l.count("FIRE")-1)}are fired!'
#     if i == 'FURY':
#         c+= f'I am {"really " * (l.count("FURY")-1)}furious.'

def determine_time(arr):
    t = 0
    for i in arr:
        h = int(i[:2])
        m = int(i[3:5])
        s = int(i[6:])
        t += h
        t += m / 60
        t += (s / 60) / 60
    if t > 24:
        return False
    return True


def nth_char(words):
    a = ''
    for i in range(len(words)):
        a += words[i][i]

    return a


# print(nth_char(['Chad','Morocco','India','Algeria','Botswana','Bahamas','Ecuador','Micronesia']))

def abbrev_name(name):
    c = name.split()
    return '{}.{}'.format(c[0][0].upper(),c[1][0].upper())


def zeros(n):
    r = list(reversed(str(math.factorial(32))))
    index = 0
    for i in range(len(r)):
        if r[i] != '0':
            index = i
            break
    return len(r[:index])

# a = 'the quick broWn fox leapt over the fence'
# c = 9
# b = list("{0:b}".format(c))
# t = b
# x = ''
# for i in a:
#     print(t)
#     if i.isalpha() and t[0] == '1':
#         x += i.swapcase()
#         t.pop(0)
#     elif i.isalpha() and t[0] == '0':
#         t.pop(0)
#         if bool(t) == False:
#             t = b
#     elif i == ' ':
#         x +=i
#
# print(x)


def binarray(s) -> int:
    if s.count(1) == s.count(0):
        return len(s)
    elif len(s) == 1 or len(s) == 0:
        return 0
    return binarray(s[1:-1])
# print(binarray([0,0,1,1,1,0,0,0,0,0]))


def duplicate_encode(word):
    c = ''
    word = word.lower()
    for i in word:
        if word.count(i) > 1:
            c += ')'
        else:
            c += '('
    print(c)
# duplicate_encode("(( @")

def reverse_list(l):
  return list(reversed(l))


def rental_car_cost(d):
    cost = 40
    total = cost * d
    if d>=7:
        total -= 50
    if d>=3 and d<7:
        total -= 20
    return total

def reverseseq(n):
    return list(range(n, 0, -1))


def balanced_num(n):
    n = [ int(i) for i in str(n)]
    if len(str(n)) < 3:
        return 'Balanced'
    elif len(n)%2 ==0:
        if sum(n[:len(n)//2-1]) == sum(n[len(n)//2+1:]):
            return 'Balanced'
        else:
            return "Not Balanced"
    elif len(n)%2 != 0:
        if sum(n[:len(n)//2]) == sum(n[len(n)//2+1:]):
            return 'Balanced'
        else:
            return "Not Balanced"

def update_light(current):
    if current == "green":
        return 'yellow'
    elif current == "yellow":
        return 'red'
    elif current == "red":
        return 'green'