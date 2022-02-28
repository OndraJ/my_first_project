TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {
        'bob': '123',
        'ann': 'pass123',
        'mike':'password123',
        'liz':'pass123'
}

line = 40*'-'

titlecase = 0
lower_words = 0
upper_words = 0
integers = []
dict_of_numbers = {}



username = input('username: ')
password = input('password: ')

if username in users.keys() and users[username] == password:
    print(line, f'Welcome to the app, {username}', 'We have 3 texts to be analyzed', line, sep='\n')
    selected_num = input('Enter a number btw. 1 and 3 to select: ')
    if not selected_num.isnumeric() or int(selected_num) < 1 or int(selected_num) > 3:
        print('Selected number must be numeric and btw. 1 and 3')
        quit()
    index_text = int(selected_num) - 1
    clear_text = [words.strip(',.') for words in TEXTS[index_text].split()]
    for i in clear_text:
        if i.istitle():
            titlecase += 1
        elif i.islower():
            lower_words += 1
        elif i.isupper():
            upper_words += 1
        elif i.isnumeric():
            integers.append(int(i))
    print(line,f'''
There are {len(clear_text)} words in the selected text.
There are {titlecase} titlecase words.
There are {upper_words} uppercase words.
There are {lower_words} lowercase words.
There are {len(integers)} numeric strings.
The sum of all the numbers {sum(integers)}
''')
    for word in clear_text:
        if len(word) not in dict_of_numbers:
            dict_of_numbers[len(word)] = 1
        else:
            dict_of_numbers[len(word)] += 1
        new_dict = dict(sorted(dict_of_numbers.items()))
    
    print(
'LEN|','OCCURENCES'.center(max(new_dict.values())),'|NR.')
    for k, v in new_dict.items():
        print(str(k).rjust(2,' '),'|',(v * '*').ljust(max(new_dict.values())),'|', str(v))
else:
    print('Unregistred user, terminating program....')
