from main import File, Catalog, CatalogFiles, sorting_by_name, sorting_by_sum_size, output_files_of_catalogs_with_PAPKA2
import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        # Библиотеки
        # Каталоги
        self.catalogs = [
            Catalog(1, 'Папка 1'),
            Catalog(2, 'Папка 2'),
            Catalog(3, 'Папка 3'),
            Catalog(11, 'Папка 1 (другая)'),
            Catalog(22, 'Папка 2 (другая)'),
            Catalog(33, 'Папка 3 (другая)'),
        ]
        # Файлы
        self.files = [
            File(1, 'Курсовая работа', 25, 1),
            File(2, 'Отчет по лабораторной работе', 35, 2),
            File(3, 'Отчет по практике', 45, 3),
            File(4, 'Реферат', 35, 3),
            File(5, 'Аннотация по АСОИУ', 25, 3),
        ]
        self.catalogs_files = [
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
        # Соединение данных один-ко-многим
        self.one_to_many = [(f.name, f.size, c.cat_name)
                            for c in self.catalogs
                            for f in self.files
                            if f.cat_id == c.id]

        # Соединение данных многие-ко-многим
        self.many_to_many_temp = [(c.cat_name, fc.cat_id, fc.file_id)
                                  for c in self.catalogs
                                  for fc in self.catalogs_files
                                  if c.id == fc.cat_id]
        self.many_to_many = [(f.name, f.size, cat_name)
                             for cat_name, cat_id, file_id in self.many_to_many_temp
                             for f in self.files if f.id == file_id]

    def test_sorting_by_name(self):
        result = sorting_by_name(self.one_to_many)
        desired_result = [('Курсовая работа', 25, 'Папка 1'), ('Отчет по лабораторной работе', 35, 'Папка 2'),
                          ('Отчет по практике', 45, 'Папка 3'), ('Реферат', 35, 'Папка 3'),
                          ('Аннотация по АСОИУ', 25, 'Папка 3')]
        self.assertEqual(result, desired_result)

    def test_sorting_by_sum(self):
        result = sorting_by_sum_size(self.one_to_many, self.catalogs)
        desired_result = [('Папка 3', 105), ('Папка 2', 35), ('Папка 1', 25)]
        self.assertEqual(result, desired_result)

    def test_output_PAPKA2(self):
        result = output_files_of_catalogs_with_PAPKA2(self.many_to_many, self.catalogs)
        desired_result = {'Папка 2': ['Отчет по лабораторной работе'], 'Папка 2 (другая)': ['Отчет по лабораторной '
                                                                                            'работе']}
        self.assertEqual(result, desired_result)
