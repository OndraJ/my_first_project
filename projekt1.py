from task_template import TEXTS

line = 40*'-'
members = {'bob' : '123', 
           'ann' : 'pass123', 
           'mike' : 'password123',
            'liz' : 'pass123'}

def checking_autorize():
    member = input('Username: ')
    password = input('Password: ')
    if member in members:
        if members[member] == password:
            print(line,
                  f'Welcome to the app, {member}',
                  'We have 3 texts to be analyzed.',
                  line, sep='\n')
        else:
            print('wrong password')
            quit()
    else:
        print('Unknown user')
        quit()

def select_text():
    number = input('Enter a number btw. 1 and 3 to select: ')
    if not number.isnumeric():
        print('Must be number')
        quit()
    elif int(number) < 1 or int(number) > 3:
        print('Wrong number')
        quit()
    else:
        print(line)
        return int(number) - 1

def cleaning_text():
    number_text = select_text()
    raw_text = TEXTS[number_text].split()
    text = []
    for char in raw_text:
        for i in ',. ':
            char = char.replace(i,'')
        text.append(char)
    return text

def is_digit(value):
    for letter in value:
        if letter.isdigit():
            return False
        else:
            return True

def text_analyse():
    global text
    text = cleaning_text()
    words = len(text)
    titlecase = [word for word in text if word.istitle()]
    uppercase = [word for word in text if word.isupper() and is_digit(word)]
    lowercase = [word for word in text if word.islower()]
    numericstring = [int(word) for word in text if word.isnumeric()]
    sum_of_num = sum(numericstring)
    print(f'''
There are {words} words in the selected text.
There are {len(titlecase)} titlecase words.
There are {len(uppercase)} uppercase words.
There are {len(lowercase)} lowercase words.
There are {len(numericstring)} numeric strings.
The sum of all the numbers {sum_of_num}
''')

def count_letters():
    len_text = []
    for char in text:
        len_char = len(char)
        len_text.append(len_char)
    return len_text

def len_of_words():
    text = count_letters()
    num_dict = {n: text.count(n) for n in text}
    return dict(sorted(num_dict.items()))

def print_frame():
    my_dict = len_of_words()
    print(f'LEN|{"OCCURENCES".center(max(my_dict.values()) + 2)}|NR.',
     line,
     sep='\n')
    for k, v in my_dict.items():
        print(str(k).ljust(2),'|',(v*"*").ljust(max(my_dict.values())),'|',str(v)+'x')

def main():
    checking_autorize()
    text_analyse()
    print_frame()

if __name__ == '__main__':
    main()