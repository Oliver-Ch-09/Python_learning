#import sympy
import math
import string
import random
#from collections import Counter


print("hello \n world \n nice \n to \n see \n you \n again \n xd ")
print(len("hello"))

mystring = "Hello World"
print(mystring[-2])
print(mystring[8])
mystring = "abcdefghijk"
print(mystring[2:])      # od punktu do końca używając :

print(mystring[:3])    # to idzie do ideksu d ale go nie wlicza

print(mystring[3:6])    # jezeli chcemy złapać coś w środku
print(mystring[1:3])

print(mystring[::])     # "od początku do końca

print(mystring[::2])   # do początku do końca, skacząc co dwa znaki  STEP SIZE

print(mystring[::-1])   # odwrócenie początku z końcem

name= "Sam"
#name[0] = P
last_letters = name[1:]
print(name[1:])
"P" + last_letters
print("p"+ last_letters)


x = "Hello World"
x = x + " it is beautifil outside"
print(x)


letter = 'z'
print(letter * 10 )


print(2+3)
print("2"+"3")   #stringi są jako znaki a nie jako liczby !!!


x = "Hello World"
print(x.upper())   #powiększenie


print(x.split())   #rozdziela słowa
x = "This is a string"
print(x)
print(x.split())   #rozdziela zdanie na poszczególne słowa
print(x.split("i"))   #rozdziela zdnaie na poszczególne słowa oraz usuwa litere "i"


print("This is a string {} " .format("INSERTED"))    #zamiast używać + można w ten sposób dodawać słowa
print("The {2} {1} {0}" .format("fox", "brown" ,"quick"))
print("The {q} {b} {f}" .format(f= "fox" ,b="brown" ,q="quick"))


result = 100/777
print(result)
print("The result was {r}" .format(r= result))
print("The result was {r:1.3f}" .format(r= result))  #zaokrąglenie f
print("The result was {r:1.5f}" .format(r= result))

name = "Adam"
print("Hello, his name is {}" .format(name))  #sposób wykorzystując format
print(f"Hello, his name is {name}")   # drugi sposób wykorzystując f przed ""

name = "Sam"
age = "3"
print(f"{name} is {age} years old")

name = "Adam"
print("My name is {}". format(name))

my_list = [1,2,3]
print(len(my_list))    #określanie długości

my_list = ["one", "two", "three"]
print(my_list[0])     #pokazanie tylko pierwszego elementu
print(my_list[0:])    #pokazanie całego zboiru od zerowego indeksu do końca

another_list = ["four", "five"]
new_list = my_list + another_list
print(new_list)
new_list[0] = "ONE ALL CAPS"
(new_list.append("six"))  # komenda append dodaje na końcu nowy element
print(new_list)
(new_list.append("seven"))
print(new_list)

new_list.pop()    #"usuwanie ostatniego elemantu"
print(new_list)

popped_item = new_list.pop()
print(popped_item)
print(new_list)

new_list.pop(0)   # fuckja pop usuwa element z listy (w zależności jaki wybierzemy poprzez indeks)
print(new_list)

new_list = ["a", "e", "x", "b", "c"]
num_list = [4, 1, 8, 3]
new_list.sort()    # funckja która sortuje w kolejności alfabetycznej
my_sorted_list = new_list
print(my_sorted_list)
num_list.sort()
print(num_list)
num_list.reverse()  #"fuckcja, która odwarca elemnty"
print(num_list)


my_dict = {"key1": "value1", "key2": "value2"}   #używanie bibliotei do określania wartości
print(my_dict)
print(my_dict["key1"])

ceny_lookup = {"apple": "2.99", "orange": "1.99", "milk": "5.88"}   # tu używamy biblioteki do sprawdzenia cen produktów
print(ceny_lookup["apple"])

d = {"k1":"123", "k2":"[0,1,2]", "k3":{"insideKEy":100}}
print(d["k2"])
print(d["k3"])

d = {"key1": ["a", "b", "c"]}
print(d["key1"])
my_list = d["key1"]  # 1 etap
print(my_list)
letter = my_list[2]   # 2 etap
print(letter)
print(letter.upper())  # 3 etap
szybsza_metoda = d["key1"][2].upper()   # wszystkie kroki możemy zrobić w jednej lini zamiast w kilku
print(szybsza_metoda)


d = {"key1":100, "key2":200}
d["key3"] = 300      # dodawanie wartości do biblioteki
print(d)
d["key1"] = "NEW VALUE"  # tak samo możemy nadpisywać już istniejące elementy w bibliotece
print(d)

d = {'key1': 100, 'key2': 200, 'key3': 300}
d.keys()
print(d.keys())
d.values()
print(d.values())
d.items()
print(d.items())



t = (1,2,3)     #tuple
my_list = [1,2,3]
t = ("a", "a", "b")
print(t.count("a"))    # ile razy pojawia sie dany element
print(t.index("a"))    # jaki jest indeks elementu
my_list[0] = "NEW"
print(my_list)
#t[0] = "NEW"     # tuple jest podobny do listy jendak w tuplu nie można nadpisywać elementów
print(t)


myset = set()   # fuckja set działa w ten sposób że dodaje element jednak taki który się nie powtarza, w tym wypadku 2
print(myset)
myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(2)
print(myset)

mylist = [1,1,1,1,2,2,2,3,3,3]   # mimo ze lista elementów jest duża SET pozwala wpisać tylko i wyłącznie jeden niepotarzający się element
print(mylist)
print(set(mylist))


True
print(type(True))   # okraslanie czy coś jest prawdą bądź fałszem

1 > 2
print(1 > 2)
1 == 1
print(1 == 1)

b = None
print(b)

myfile = open("myfile.txt")
print(myfile.readlines())
print(myfile.readlines())   # przy drugim odczycie nie pojawi sie zdanie a tylko nawiasy. Zeby to naprawić trzeba zresetować kursor poprzez funkcje seek
myfile.seek(0)
print(myfile.readlines())

myfile.seek(0)                # dwa rodzaje odczytu poprzez READ albo READLINES
print(myfile.read())
myfile.close()

with open("myfile.txt") as my_new_file:
    my_new_file.seek(0)
    contents = my_new_file.read()
    print(contents)

with open("myfile.txt",mode="r") as myfile:
    contents = myfile.read()

with open("myfile.txt",mode="r") as myfile:
    contents = myfile.read()

print("\n")

newfile = open("newfile")
print(newfile.readlines())

with open("newfile", mode="r") as f:      # mod r służy do odczytu
    print(f.read())

#with open("newfile", mode="a") as f:    # mod a słyzy do dodawania elementów
    #f.write("\nFOUR ON FOURTH")

with open('sdafsafsaf.txt', mode='w') as f:      # mod w służy do nadpisywania elementów
    f.write('I CREATED THIS FILE!')

with open('sdafsafsaf.txt', mode='r') as f:
    print(f.read())

print("\n")

print( 2 == 2 )
print("hello" == "bye")
print("Bye" == "bye")
print(2.0 == 2)
print(4!=5)
print(2>1)
print(2<5)
print(2>=2)
print(4<=1)

print(1<2)
print(2<3)
print(1<2<3)
print(1<2 and 2<3)

print("\n")

print('h' == 'h' and 2==2)    # przy fukcji "AND" wystaczy ze jedno równanie nie jest prawdą zeby pokazało fałsz

print(100 == 1 or 2 == 2)   # przy fukcji "OR" wystaczy ze jedno równanie jest prawdą zeby pokazało prawde

print(1 == 1)
print(not 1 ==1 )
print(400 > 5000)
print( not 400 > 5000)  #wstawiająć funkcje NOT wynik jest przeciwny do prawdziwego wieć 400 > 5000 jest prawdą

print("\n")

if True:
    print("ITS TRUE")

if 3>2:
    print("ITS TRUE")

hungry = True      # oświadczenie prawda przy fukcji IF zaskutkuje pojawianiem sie wyniku
if hungry:
    print('FEED ME!')

hungry = False       # oświadczenie fałsz zaskutkuje nie pojawieniem sie wyniku jednak uzywając funkcji ELSE fajawi sie wynik dla fałszu
if hungry:
    print('FEED ME!')
else:
    print("Im not hungry")

print("\n")

loc = "Store"
if loc == "Auto Shop":              # jeżeli lokalizacja jest przypisana do jakiegość miesjca wynikiem bedzie print, jednak jęzeli nie bedzie istniejącej lokalizacji fukcja ELSE wyprintuje I do not know much
    print("Cars are cool")
elif loc == "Bank":
    print("Money is cool!")
elif loc == "Store":
    print("Welcome to the store!")
else:
    print("I do not know much.")

print("\n")

name = "Sammy"         # Jezeli imie to Sammy wyprintuj Hello Sammy (tak samo Frankie) a jeżeli bedzie to coś innego to zapyta jak masz na imie.
if name == "Frankie":
    print("Hello Frankie")
elif name == "Sammy":
    print("Hello Sammy")
else:
    print("What is your name?")

print("\n")

my_interable = [1,2,3]
for item_name in my_interable:
    print(item_name)


mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)

mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print("Hello")


for num in mylist:   # jezeli liczba jest podzielna przez w tym przypadku 2 to wyprintuj wynik
    if num %2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')         # dla reszty która nie spełnia warunku wyprintuj dodając Odd Number

print("\n")
list_sum = 0

for num in mylist:
    list_sum = list_sum + num
    print(list_sum)  # tutaj wyprintowuje kazdy etap po kolei, ponieważ fuckja print jest zliniowana z loopem

print(list_sum)   # tu wpypisze tylko końcowy wynik sum czyli 55

mystring = "Hello World"
for letter in mystring:
    print(letter)


for letter in "Hello World":        # można też to zrobić bez przypisywania stringa do jakiejś zmiennej
    print(letter)


tup = (1,2,3)
for item in tup:
    print(item)

mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))

for item in mylist:
    print(item)

for a,b in mylist:   # przypisując zmienne np. a i b można roldzielić tuple i wybrać to co konkretnie chcemy w tym przypadku
    print(a)        # a = 1,3,5,7, b= 2,4,6,8
    print(b)

print("\n")

mylist = [(1,2,3),(5,6,7),(8,9,10)]
for a,b,c in mylist:
    print(b)

print("\n")


d = {"k1":1,"k2":2,"k3":3}

for key,value in d.items():
    print(key)

print("\n")

x = 0
while x < 5:
    print(f"The current value of x is {x}")
    #x = x+1    # mozna to zapisać dwojako x = x+1 albo x +=1 TO TO SAMO
    x += 1
else:
    print('X IS NOT LESS THEN 5')

print("\n")

x = [1,2,3,4,5]
for item in x:
    pass            # fukcje PAS wstawiamy kiedy chcemy na później zostawić sobie kod ale nie chcemy zeby wyskakiwały błedy

print("\n")

mystring = 'Sammy'
for letter in mystring:        # fuckja continue pozwala na dokończenie fuckji
    if letter == 'a':
        continue
    print(letter)

print("\n")

mystring = 'Sammy'
for letter in mystring:         # fuckja break zatrzymuje lupa i go konczy na elemencie który wskazaliśmy
    if letter == 'a':
        break
    print(letter)

print("\n")

x = 0
while x<5:          # fukcja wyprintowuje po kolei liczby jednak fukcja BREAK na liczbie 2 zatrzymuje lupa
    if x == 2:
        break
    print(x)
    x = x+1

print("\n")


mylist = [1, 2, 3]
for num in range(0, 10, 2):       # fuckja in range określa zasięg działania fuckji. W tym przypadku od 0 do 10 ALE liczby podzielne przez 2 (plus nie uwzględnia 10)
    print(num)

print("\n")

index_count = 0                 # kod ten okresla jaki jest indeks dla poszczególnej litery
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

word = 'abcde'
for index, letter in enumerate(word):       # tu tak samo określa jaki jest indeks dla litery ale poprzez tuple
    print(index)
    print(letter)
    print('\n')


mylist1 = [1,2,3]
mylist2 = ['a','b','c']                 # fuckja zip łączy ze sobą poszczególne listy
mylist3 = [100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)

print(list(zip(mylist1,mylist2)))

print("\n")

print(2 in [1,2,3])                 #sprawdzanie czy dany element jest w tabeli, bibliotece itd.
print('x' in ['x', 'y','z'])

print('a' in 'a world')

print('\n')

mylist = [10,20,30,40,100]          # pokazywanie maklsymalnych i minimalnych wartości z listy
print(min(mylist))
print(max(mylist))

from random import shuffle          # pobralismy z randomowej biblioteki funkcje shuffle która miesza nam elementy w liście
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)

print('\n')

from random import randint      #fuckja randint łapie randomową liczbe z listy i ją oddaje
print(randint(0,100))

#result = float(input('What is your favorite number'))        #input przedstawi wszystko jako stringi chyba ze podamy ze ma np, pokazac jako liczbe fuckją INT albo FLOAT
print(result)
print(type(result))

print('\n')


mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)


mylist = [letter for letter in mystring]
print(mylist)

mylist = [x for x in 'word']
print(mylist)

mylist = [x**2 for x in range(0,11)]
print(mylist)


mylist = [x**2 for x in range(0,11) if x%2==0]
print(mylist)

celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))
print(fahrenheit)


result = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(result)

mylist = []
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)
print(mylist)


# TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST TEST
print('\n')
print('\n')


str_ = 'Print only the words that start with s in this sentence'         # oddaje słowa które zaczynają sie na literę S
for word in str_.split():
    if word[0] == 's':
        print(word)


mylist = [x for x in range(0,11) if x%2==0]             # oddaje wszystkie liczby parzyste
print(mylist)

print([x for x in range(0,11,2)])
print(list(range(0,11,2)))                      # taki sam wynik 3 różne sposoby
for num in range(0,11,2):
    print(num)



idn = [x for x in range(1,51) if x%3==0]
print(idn)


str_ = 'Print only the words that start with s in this sentence'
for word in str_.split():
    if len(word) % 2 == 0:
        print(word)

for num in range(0,101):
    if num%3 and num%5 == 0:
        print("FizzBuzz")
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)


st = 'Create a list of first letters of every word in this string'
print([word[0] for word in st.split()])


print([x for x in range(0,11,2)])
print(list(range(0,11,2)))
for num in range(0,11,2):
    print(num)

# KONIEC TESTU

print('\n')



def name_function():        #definiowanie fuckji
    """"
    DOCSTRING: Informacje na temat fuckji
    INPUT: no input
    OUTPUT: Hello
    """
    print('Hello')                          # dodatkowa informajcja przy punkcji help

help(name_function())


def say_hello(name = 'Name'):
    return 'Hello' + ' ' + name

result = say_hello('Sally')
print(result)


def add(n1,n2):
    return n1+n2
result = add(20,30)
print(result)


#Find our is the word 'dog' is in a string ?
def dog_check(mystring):
    return 'dog' in mystring.lower()

print(dog_check('Dog ran away'))




def pig_latin(word):

    first_letter = word[0]

    if first_letter in 'aeiou':
        pig_word = word + "ay"
    else:
        pig_word = word[1:] + first_letter + "ay"
    return pig_word


z = pig_latin('apple')
print(z)

# ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA

#ZADANIE

print('\n')

def myfunc(name):
    print("My name is {}".format(name))

myfunc("Oliwer")


#ZADANIE 3
def myfunc(a):
    if a == True:
        return 'Hello'
    elif a == False:
        return "Goodbye"

print(myfunc(False))

#ZADANIE 4
def myfunc(x,y,z):
    if z == True:
        return x
    elif z == False:
        return y

print(myfunc('Hello', 'Goodbye', True))


#ZADANIE 5

def myfunc(a,b):
    return a*b

print(myfunc(3,4))


#ZADANIE 6

def myfunc(int):
    if int%3 == 0:
        return True
    else:
        return False

print(myfunc(6))

#ZADANIE 7

def is_greater(a,b):
    if a>b:
        return 'Prawda'
    elif a <= b:
        return False

print(is_greater(6,3))

print('\n')

def myfunc(a,b,c=0,d=0,e=0):            # przy 6 elementach pokaże sie error dlatego korzysta się z fukcji args
    return sum((a,b,c,d,e))*0.05
print(myfunc(40,60,100))


def myfunc(*args):
    return sum(args)*0.05
print(myfunc(40,60))


def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
print(myfunc(fruit='apple', veggie = 'lettuce'))


def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {} '.format(args[0],kwargs['food']))

myfunc(10,20,30,fruit = 'orange', food='eggs',animal = 'dog')


#ZADANIE 8

def myfunc(*args):
    return sum(args)

print(myfunc(1,2,3,4))

#ZADANIE 9

def myfunc(*args):
    list =[]
    for arg in args:
        if arg % 2 == 0:
            list.append(arg)
    return list

print(myfunc(5,6,7,8))

#'Anthropomorphism'

#ZADANIE 10


def myfunc(string):
    slowo = ''
    for i in range(len(string)):
        if i % 2 == 1:
            slowo += string[i].upper()
        else:
            slowo += string[i].lower()
    return slowo


print(myfunc('Anthropomorphism'))

print('\n')
#ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA

#ZADANIE1       Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two_evens(8,2))


#ZADANIE 2      Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]

print(animal_crackers('Levelheaded Plama'))


#ZADANIE 3      Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(n1,n2):
    return (n1+n2) == 20 or n1 == 20 or n2 == 20

print(makes_twenty(3,2))

#ZADANIE 4      Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    if len(name) >3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return "Name is too short"

print(old_macdonald('macdonald'))


#ZADANIE 5      Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    return ' '.join(text.split()[::-1])
print(master_yoda("Here am I"))


#ZADANIE 6          Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):            # od 190 do 210 i od 90 do 110 jest okey reszta false
    if n in range(190,211):
        return True
    elif n in range(90,111):
        return True
    else:
        return False


print(almost_there(90))
print('\n')
#ZADANIE 7      Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    else:
        return False

print(has_33([1,3,3,2,4]))


#ZADANIE 8      Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    result = ''
    for char in text:
        result += char*3
    return result

print(paper_doll('Hello'))

#ZADANIE 9 Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
            # Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a,b,c):
    if a+b+c <= 21:
        return a+b+c
    elif a+b+c > 21 and a==11 or b==11 or c==11:
        z = a+b+c-10
        if z >21:
            return 'BUST'
        else:
            return a+b+c-10
    elif a+b+c >21 and a!=11 or b!=11 or c!=11:
        return 'BUST'


print(blackjack(9 ,9,9))
print('\n')

#ZADANIE 10   Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr_ : list):
    wynik = 0
    for num in arr_:
        if  num in range(6,10):
            continue
        wynik += num
    return wynik

print(summer_69([4,5,6,7,8,9]))

#ZADNIE 11      Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    range_ = len(nums)-2
    for i in range(0, range_):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False

def spy_game(nums):
    search = "007"
    str_ = ""
    for num in nums:
        string = str(num)
        str_ += string

    if search in str_:
        return True
    return False

print(spy_game([1,2,3,4,5,0,0,7]))

#ZADANIE 12  Write a function that returns the number of prime numbers that exist up to and including a given number

#a = len(list(sympy.primerange(0,100)))
#print(a)


#ZADANIE 13  Write a function that takes in a single letter, and returns a 5x5 representation of that letter
def litera_big(letter):
    big = {
        'a': "  *\n * *\n*****\n*   *\n*   *\n"
    }
    return big[letter]

print(litera_big('a'))

print('\n')

def square(num):
    return num**2

my_nums = [1,2,3,4,5]
#print(map(square, my_nums))
for item in map(square,my_nums):
    print(item)

print(list(map(square,my_nums)))

def splicer(mystring):              # fukcja MAP łączy np, zdefiniowaną fuckje z jakąs listą
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer,names)))


def check_even(num):
    return num%2 == 0
mynums = [1,2,3,4,5,6]
print(list(filter(check_even, mynums)))

for n in filter(check_even, mynums):
    print(n)


def square(num):
    result = num ** 2
    return result
print(square(3))


print('\n')

lambda num: num**2
print(square(2))

list(map(lambda num: num ** 2, mynums))

list(filter(lambda  num: num%2 == 0, mynums))

list(map(lambda  x:x[::-1], names))

print('\n')

x = 25

#def printer():
    #x = 50
    #return x

print(x)
#print(printer())


#GLOBAL
name = 'This is a global string'
def greet():

    # ENCLOSING
    name = 'Sammy'
    def hello():
        #LOCAL
        name = 'IM A LOCAL'
        print('Hello '+ name)

    hello()

print(greet())

print('\n')

x = 50
def func():
    global x
    print(f'X is {x}')

    # LOCAL REASSIGNMENT ON A GLOBAL VERIABLE !
    x= 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')

print(func())

print('\n')
# ZADANIA ZADANIE ZADANIA ZADANIA ZADANIE ZADANIA ZADANIA ZADANIE ZADANIA ZADANIA ZADANIE ZADANIA
#ZADANIE 1
def vol(rad):
    return 4/3 *3.1415*(rad**3)

print(vol(2))

#ZADANIE 2

def ran_check(num, low, high):
    for i in range(low, high+1):
        if num >= low and num <= high:
            return f'{num} is in the range between {low} and {high}'
        else:
            return f'{num} is not in the range between {low} and {high}'


print(ran_check(4,0,4))

#ZADANIE 3

#zdanie = 'Hello Mr. Rogers, how are you this fine Tuesday ?'

def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])

print(up_low('Hello Mr. Rogers, how are you this fine Tuesday ?'))

#ZADANIE 4

def unique_list(lst):
    return set(lst)

print(unique_list([1,1,1,1,2,2,2,2,3,3,3,4,4,4,6,7,7,7,8]))

#ZADANIE 5

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


print(multiply([1,2,3,-4]))

#ZADANIE 6

def palindrome(zdanie):
    zdanie = zdanie.replace(' ','')         # usuwa spacje które zapsuły by wynik
    if zdanie == zdanie[::-1]:
        return 'YEY IT IS PALINDROME'
    else:
        return 'IT IS NOT PALINDROME'

print(palindrome('nurses run'))

#ZADANIE 7

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))


print('\n'*2)

class Dog():

    species = 'mammal'

    def __init__(self, breed, name):

        self.breed = breed
        self.name = name

    def bark(self, number):
        print('WOOF! My name is {} and the number is {}'.format(self.name, number))


my_dog = Dog(breed='Lab', name = 'Sammy')

print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)
print(my_dog.bark(10))


print('\n'*2)


class Circle():

    pi = 3.14

    def __init__(self, radius=1):

        self.radius = radius
        self.area = radius * radius * Circle.pi


    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)

print('\n')

class Animal():
    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')


myanimal = Animal()
print(myanimal)

print(myanimal.eat())
print(myanimal.who_am_i())

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    def eat(self):
        print('I am a dog and eating')

    def bark(self):
        print('WOOF!')

mydog = Dog()
print(mydog.eat())
print(mydog.who_am_i())
print(mydog.bark())


print('\n'*2)


class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name +' says meow!'

niko = Dog('niko')
felix = Cat('felix')
print(niko.speak())
print(felix.speak())

print('\n')

for pet in [niko, felix]:

    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

print(pet_speak(niko))
print(pet_speak(felix))

class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract methon')

class Dog(Animal):

    def speak(self):
        return self.name + ' says woof!'


class Cat(Animal):

    def speak(self):
        return self.name + ' says moew!'

fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())

print('\n'*3)



mylist = [1,2,3]
print(len(mylist))

class Sample():
    pass

mysample = Sample()
print(mysample)


class Book():

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    #def __del__(self):
        print("A book object has been deleted")

b = Book('Python rock' , 'Jose', 200)


class Dog(Animal):

    def speak(self):
        return self.name + ' says woof!'
print(b)
print(str(b))
print(len(b))




print('\n'*4)

# ZADANIE ZADANIA ZADANIA ZADANIA ZADANIE ZADANIA ZADANIA ZADANIA ZADANIE ZADANIA ZADANIA ZADANIA ZADANIE ZADANIA

class Line:

    def __init__(self, coor1, coor2):

        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        z1 = (coordinate2[0]-coordinate1[0])**2
        z2 = (coordinate2[1]-coordinate1[1])**2
        z3 = z1 + z2

        return math.sqrt(z3)

    def slope(self):

        return (coordinate2[1] - coordinate1[1]) / (coordinate2[0] - coordinate1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)
li.distance()
li.slope()
print(li.distance())
print(li.slope())



# ZADANIE 2

class Cylinder():
    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        return 3.14*self.radius**2 * self.height

    def surface_area(self):
        return 2*3.14*self.radius* self.height + 2*3.14*self.radius**2

c= Cylinder(2,3)
c.volume()
c.surface_area()
print(c.volume())
print(c.surface_area())


# ZADANIE ZADANIE ZADANIE ZADANIE ZADANIE ZADANIE ZADANIE ZADANIE ZADANIE ZADANIE ZADANIE ZADANIE
print('\n'*3)

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def information(self):
        print('Account owner: {} \nAccount balance: {}$'.format(self.owner, self.balance))

    def add_to_bank(self, value):

        self.balance = self.balance + value
        print("We just added {}$ to your account. Now you have {}$ ".format(value, self.balance))


    def take_from_bank(self, money):

        if self.balance > 0 and self.balance > money:
            self.balance = self.balance - money
            print("You just withdraw {}$ from your account.".format(money))
        else:
            print("You can't withdraw {}$. Your account has only {}$".format(money, self.balance))



act1 = Account('Jose', 500)
act1.information()
act1.add_to_bank(300)
act1.take_from_bank(900)
act1.take_from_bank(100)
act1.information()


print('\n'*3)


def add(n1,n2):
    print(n1+n2)

add(10,20)

number1 = 10
#number2 = input('Please provide a number')
#print(add(number1, number2))
#print('Something happend')

try:
    result = 10 + 10
except:
    print("Hey it loooks like you aren't adding correcly")
else:
    print('Add went well!')
    print(result)

print("\n"*3)

try:
    f = open('testfile', "r")
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error")
finally:
    print("I always run")

print("\n"*3)

def ask_for_int():

    while True:
        try:
            result = int(input("Please provide number:"))
        except:
            print("Whoops ! That is not a number")
            continue
        else:
            print("Yes thank your number is {}".format(result))
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end!")
#ask_for_int()


#ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA

#ZADANIE 1
try:
    for i in ["a", "b", "c"]:
        print(i**2)
except:
    print("Dude you messed up!")

#ZADANIE 2

x = 5
y = 0
try:
    z = x/y
except:
    print("NIE DZIEL CHOLERO PRZEZ ZERO")
finally:
    print("All Done!")

#ZADANIE


def square_of_number():
    while True:
        try:
            number = int(input("Please provide number!"))
            square = number ** 2
        except:
            print("An arror accurred! Please try again!")
        else:
            print("Thank you, your number squared is: {}".format(square))
            break

#square_of_number()
print("\n"*3)

def func():
    return 1

func()

def hello():
    return "Hello"

hello()


def hello(name="Jose"):
    print("The hello() function has been executed!")

    def greet():
        return "\t This is the greet() func inside hello!"                 #  /t odpowiada tab

    def welcome():
        return "\t This is welcome() inside hello"

    print("I am going to reuturn fucntion!!")

    if name == "Jose":
        return greet()
    else:
        return welcome()

my_new_func = hello("Jose")
print(my_new_func)


def cool():

    def super_cool():
        return "I am very cool!"

    return super_cool()

some_func = cool()
print(some_func)


print("\n"*3)


def hello():
    return "Hi Jose!"

def other(some_def_func):
    print("Other code runs here!")
    print(some_def_func)

other(hello())

print("\n"*3)


def new_decorator(original_func):

    def wrap_func():

        print("Some extra code, before the original function")

        original_func()

        print("Some extra code, after the original function!")

    return wrap_func()

def func_needs_decorator():
    print("I wan to be a decorated!")

decorated_func = new_decorator(func_needs_decorator)


print("\n"*2)


@new_decorator
def func_needs_decorator():
    print("I wan to be a decorated!")

func_needs_decorator


def create_cubes(n):
    for x in range(n):
        yield x**3

for x in create_cubes(10):
    print(x)


def gen_fibon(n):

    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for number in gen_fibon(10):
    print(number)


def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()
print(g)
print(next(g))
print(next(g))
print(next(g))


s = "Hello"
for letter in s:
    print(letter)

s_iter =iter(s)
print(next(s_iter))

print("\n"*3)

#ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA ZADANIA


#ZADANIE 1
def gensquares(n):
    for x in range(n):
        yield x**2

for x in gensquares(10):
    print(x)

#ZADANNIE 2

print("\n"*2)

def rand_num(low,high,n):
    for number in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)

print("\n"*2)

#ZADANIE 3


s = "hello"
s = iter(s)
print(next(s))


print("\n"*2)

from collections import Counter

l = [1,1,1,1,1,2,2,2,2,3,3,3,3]         # ile pojawia się poszczególnych liczb
print(Counter(l))

s = "dsadsadsadsadasvas"                # ile pojawia sie poszczególnych liter
print(Counter(s))

s = "How many time does each word show up in this sentence word word shoe up up"     #mozemy policzyć ile słów jest w danym zdaniu
words = s.split()
print(Counter(words))

c = Counter(words)
print(c.most_common(2))                     #pokazuje jakie dwa słowa(w tym przypadku) wystepują
print(sum(c.values()))                      # suma wszystkich słów

print("\n"*3)

from collections import defaultdict

d= {"k1":1}
print(d['k1'])
d = defaultdict(object)
print(d["one"])

for item in d:
    print(item)

d = defaultdict(lambda: 0)
print(d["one"])
d["two"] = 2
print(d)


d = {}

d["a"] = 1
d["b"] = 2
d["c"] = 3
d["d"] = 4
d["e"] = 5
print(d)

for k,v in d.items():
    print(k,v)

print("\n"*2)

from collections import OrderedDict
d = OrderedDict()
d["a"] = 1
d["b"] = 2
d["c"] = 3
d["d"] = 4
d["e"] = 5
for k,v in d.items():
    print(k,v)

d1 = OrderedDict()
d1["a"] = 1
d1["b"] = 2
                        # te dwie biblioteki mimo ze są takie same przy OrderDict już takie nie są, wiec przy ich porównaniu pokaże sie stejtment False jednak gdyby były to normalne biblioteki stajtment byłby True
d2 = OrderedDict()
d2["b"] = 2
d2["a"] = 1

print(d1 == d2)


print("\n"*2)

t = (1,2,3)
print(t[0])

from collections import namedtuple

Dog = namedtuple("Dog", "age breed name")

sam = Dog(age=2, breed= "Lab", name= "Sammy")
print(sam.age)
print(sam[0])


Cat = namedtuple("Cat", " fur claws name")
c = Cat(fur="Fuzzy", claws=False, name = "Kitty")
print(c.name)
print(c.claws)

# TESTY TESTY TESTY TESTY TESTY TESTY TESTY TESTY TESTY TESTY TESTY TESTY TESTY TESTY TESTY TESTY TESTY TESTY TESTY
text = open("C:\\Users\\Oliwer Chmielowski\\Desktop\\text1.txt")
print(text.readlines())


with open("C:\\Users\\Oliwer Chmielowski\\Desktop\\text1.txt", mode="a") as f:
    f.write( "\n" "Dodanie nowego tekstu przez pythona")