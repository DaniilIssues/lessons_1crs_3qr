import csv
from pprint import pprint
import re

data = ['info_1.txt', 'info_2.txt', 'info_3.txt']
key_words = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
os_prod_list = []
os_name_list = []
os_code_list = []
os_type_lis = []
general_list = [os_prod_list, os_name_list, os_code_list, os_type_lis]


def get_data(in_data, list_in, keys):
    main_data = []
    for file in in_data:
        with open(file) as f:
            for str_file in f:
                for num, key in enumerate(keys):
                    if re.match(key, str_file):
                        a = re.split(r':', str_file)
                        list_in[num].append(a[1].strip())

    main_data.append(keys)

    for i in range(len(list_in) - 1):
        main_data.append([])
        for k, v in enumerate(list_in):
            main_data[i + 1].append(v[i])

    return main_data


# pprint(get_data(data, general_list, key_words))


def write_to_csv(csv_file, in_data, list_in, keys):
    main_data = get_data(in_data, list_in, keys)
    with open(csv_file, 'w') as f:
        f_n_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        f_n_writer.writerows(main_data)


write_to_csv('test.csv', data, general_list, key_words)
