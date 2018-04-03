import sqlite3


class Model:
    """ Взаимодействие с базами данных """
    def __init__(self, curs, spec, group):
        self.curs = curs
        self.spec = spec
        self.group = group

    def sql_select(self):
        """Есть папки курсов. В них есть базы данных специальностей этого курса. В каждой бд есть таблицы групп
        Например: curs_2/spec_123.db (Таблица io61 в этой базе данных)"""
        conn = sqlite3.connect('database\\curs_{}\\spec{}_v2.db'.format(self.curs, self.spec))  # конект к базе данных
        cursor = conn.execute('SELECT * FROM {} ORDER BY id;'.format(self.group.replace('-', '').lower()))  # запрос
        result = cursor.fetchall()  # в переменную присваиваем результата запроса
        # print(result)
        conn.close()  # дисконектимся от базы данных

        return result

    def sql_columns_names(self):
        """Возвращает названия столбцов"""
        conn = sqlite3.connect('database\\Curs_{}\\spec{}_v2.db'.format(self.curs, self.spec))
        cursor = conn.execute('SELECT * FROM {};'.format(self.group.replace('-', '').lower()))  # делаем запрос
        columns_names = [desc[0] for desc in cursor.description]  # получаем название стобцов
        # print(columns_names)
        conn.close()  # дисконектимся от базы данных

        return columns_names

    def sql_delete(self, number):
        """ Удаление студента с базы данных """
        conn = sqlite3.connect('database\\curs_{}\\spec{}_v2.db'.format(self.curs, self.spec))
        conn.execute('DELETE FROM {} WHERE id = {};'.format(self.group.replace('-', '').lower(), number))
        conn.commit()
        # print('deleted')
        conn.close()

    def sql_insert(self, info):
        """ Добавление студента в базу данных """
        conn = sqlite3.connect('database\\curs_{}\\spec{}_v2.db'.format(self.curs, self.spec))
        # print('INSERT INTO {} VALUES (?, ?, ?);'.format(group.replace('-', '').lower(), number, name, marks))
        conn.execute('INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'.
                     format(self.group.replace('-', '').lower()), info)
        conn.commit()
        # print('inserted')
        conn.close()

    def sql_average(self):
        conn = sqlite3.connect('database\\Curs_{}\\spec{}_v2.db'.format(self.curs, self.spec))  # конект к базе данных
        cursor = conn.execute('SELECT AVG(mark_1), AVG(mark_2), AVG(mark_3), AVG(mark_4), AVG(mark_5), AVG(mark_6),'
                              ' AVG(mark_7), AVG(mark_8), AVG(mark_9), AVG(mark_10) FROM {};'
                              .format(self.group.replace('-', '').lower()))  # делаем запрос
        result = cursor.fetchall()
        # print(result)
        conn.close()  # дисконектимся от базы данных
        return result


if __name__ == '__main__':
    new = Model(int(input('curs: ')), input('spec: '), input('group: '))
    data = new.sql_select()
    print(new.sql_columns_names())
    for row in data:
        print(row)
    new.sql_delete(input('Delete id:'))
    print('Create student:')
    new.sql_insert([input() for i in range(12)])
