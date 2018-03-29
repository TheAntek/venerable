import sqlite3


class Model:
    """ Взаимодействия с базами данных """
    def __init__(self, curs, spec, group):
        self.curs = curs
        self.spec = spec
        self.group = group

    def select(self):
        """ Возвращает все ряды таблицы """
        conn = sqlite3.connect('database\\curs_{}\\spec{}_v2.db'.format(self.curs, self.spec))
        cursor = conn.execute('SELECT * FROM {}'.format(self.group.replace('-', '').lower()))
        result = cursor.fetchall()
        conn.close()
        return result

    def columns(self):
        """ Возвращает названия всех столбцов таблицы """
        conn = sqlite3.connect('database\\Curs_{}\\spec{}_v2.db'.format(self.curs, self.spec))
        cursor = conn.execute('SELECT * FROM {}'.format(self.group.replace('-', '').lower()))
        columns_names = [desc[0] for desc in cursor.description]  # получаем название стобцов
        conn.close()
        return columns_names


if __name__ == '__main__':
    new = Model(int(input('curs: ')), input('spec: '), input('group: '))
    new.select()
    new.columns()
