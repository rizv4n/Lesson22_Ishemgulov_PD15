# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля

import operator

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(data):
    d_list = []
    for line in data.split('\n'):
        name, age = line.split(';')
        d_list.append({'name': name, 'age': int(age)})
    return d_list


def _sort(data):
    return sorted(data, key=operator.itemgetter('age'))


def _filter(data):
    return [[i['name'], i['age']] for i in data if int(i['age']) > 10]


def get_users_list(data):
    data_r = _read(data)
    data_s = _sort(data_r)
    return _filter(data_s)


if __name__ == '__main__':
    print(get_users_list(csv))
