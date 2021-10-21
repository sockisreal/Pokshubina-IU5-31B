# используется для сортировки
from operator import itemgetter

class File:
    """ Файл """
    def __init__(self, id, name, size, cat_id):
        self.id = id
        self.name = name
        self.size = size
        self.cat_id = cat_id

class Catalog:
    """Каталог файлов"""
    def __init__(self, id, cat_name):
        self.id = id
        self.cat_name = cat_name

class CatalogFiles:
    """ Файлы каталога для реализации связи многие-ко-многим """
    def __init__(self, cat_id, file_id):
        self.cat_id = cat_id
        self.file_id = file_id

# Каталоги
catalogs = [
    Catalog(1, 'Папка 1'),
    Catalog(2, 'Папка 2'),
    Catalog(3, 'Папка 3'),
    Catalog(11, 'Папка 1 (другая)'),
    Catalog(22, 'Папка 2 (другая)'),
    Catalog(33, 'Папка 3 (другая)'),
]
# Файлы
files = [
    File(1, 'Курсовая работа', 25, 1),
    File(2, 'Отчет по лабораторной работе', 35, 2),
    File(3, 'Отчет по практике', 45, 3),
    File(4, 'Реферат', 35, 3),
    File(5, 'Аннотация по АСОИУ', 25, 3),
]
catalogs_files = [
    CatalogFiles(1, 1),
    CatalogFiles(2, 2),
    CatalogFiles(3, 3),
    CatalogFiles(3, 4),
    CatalogFiles(3, 5),
    CatalogFiles(11, 1),
    CatalogFiles(22, 2),
    CatalogFiles(33, 3),
    CatalogFiles(33, 4),
    CatalogFiles(33, 5),
]

def main():
    """Основная функция"""
    # Соединение данных один-ко-многим
    one_to_many = [(f.name, f.size, c.cat_name)
                   for c in catalogs
                   for f in files
                   if f.cat_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.cat_name, fc.cat_id, fc.file_id)
                         for c in catalogs
                         for fc in catalogs_files
                         if c.id == fc.cat_id]
    many_to_many = [(f.name, f.size, cat_name)
                    for cat_name, cat_id, file_id in many_to_many_temp
                    for f in files if f.id == file_id]
    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все каталоги
    for c in catalogs:
        # Список файлов каталога
        c_files = list(filter(lambda i: i[2] == c.cat_name, one_to_many))
        # Если каталог не пустой
        if len(c_files) > 0:
            # Размеры файлов каталога
            c_sizes = [size for _, size, _ in c_files]
            # Суммарный размер файлов каталога
            c_sizes_sum = sum(c_sizes)
            res_12_unsorted.append((c.cat_name, c_sizes_sum))
    # Сортировка по суммарному размеру
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все каталоги
    for c in catalogs:
        if 'Папка 2' in c.cat_name:
            # Список файлов каталога
            c_files = list(filter(lambda i: i[2] == c.cat_name, many_to_many))
            # Только название файлов
            c_files_names = [x for x, _, _ in c_files]
            # Добавляем результат в словарь
            # ключ - каталог, значение - список названий
            res_13[c.cat_name] = c_files_names
    print(res_13)

if __name__ == '__main__':
    main()
