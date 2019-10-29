array = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w') as f_in:
    for i in array:
        f_in.write(i)

print(f_in)     # по умолчанию кодировка cp1251

with open('test_file.txt', encoding='utf-8') as f_out:
    print(f_out)
    for i in f_out:
        print(i)
