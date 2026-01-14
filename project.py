numbers1 = [1, 2, 3, 4, 5]
numbers2 = list([1, 2, 3, 4, 5])
if numbers1 == numbers2:
    print("list same")
else:
    print("list not same")

subject = ["math", "chemistry", "geography", "liter", "APS"]
subject[0] = 'Russian'
print(subject)

guestList = ["Nuradil", "Kemal", "Suleiman", "karim"]
print(guestList[2])
print(guestList[0])
print(guestList[-1])

list = []
print(list)

guestList = ["Nuradil", "Kemal", "Suleiman", "karim"]
name = "Kamri"
if name in guestList:
    print(f"{name} have in list")
else:
    print(f"{name} not in list")

emptyString = ''
if emptyString == '':
   print('Строка пуста')

str1 = 'Привет,'
str2 = 'Мир!'
message = (str1 + ' ' + str2)
message += ' \n Как дела?'
print(message)

pechat = """
A: Where are you?
B: I am in toronto!
A: what street?
B: I live in Downtown 
"""
print(pechat)

num = "5" + "3"
val = int(num) * 2
print(float(val))

num = "3" + "2"
sum = int(num) + int(num)
sum2 = sum / 3
print(sum2)

string = "Эта строка для теста"
symbol1 = string[0]  # Э
print(symbol1)
symbol9 = string[8]  # о
print(symbol9)


print("a" * 3)
print("so" * 5)

a = 4
b = 5
print(f"If a-{a} and b-{b} is a+b-{a+b}")

name = 'Kemal'
age = 19
street = 'finch 117'
print(f'{name} is {age} years old, live in {street}')

greeting = 'урок начинается'
print(greeting)
helloclass = 'привет класс'
print(helloclass)

fullgreating = ("рок начинается. "
                "слушаем внимательно "
                "good morning")
print(fullgreating)

joke = '''
A: why are you ask?
B: do you wish ask?
'''
print(joke)

message = "word \"Hello world!\" , is very popular in \\IT"
print(message)