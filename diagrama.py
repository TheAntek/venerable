import matplotlib.pyplot as plt
import sqlite3


def sql_columns_names(curs, spec, group):
    """Возвращает названия столбцов"""
    conn = sqlite3.connect('database\\Curs_{}\\spec{}_v2.db'.format(curs, spec))  # конектимся к базе данных
    cursor = conn.execute('SELECT * FROM {};'.format(group.replace('-', '').lower()))  # делаем запрос
    columns_names = [desc[0] for desc in cursor.description]  # получаем название стобцов
    # print(columns_names)
    conn.close()  # дисконектимся от базы данных

    return columns_names


def sql_average(curs, spec, group):
    conn = sqlite3.connect('database\\Curs_{}\\spec{}_v2.db'.format(curs, spec))  # конектимся к базе данных
    cursor = conn.execute('SELECT AVG(mark_1), AVG(mark_2), AVG(mark_3), AVG(mark_4), AVG(mark_5), AVG(mark_6),'
                          ' AVG(mark_7), AVG(mark_8), AVG(mark_9), AVG(mark_10) FROM {};'
                          .format(group.replace('-', '').lower()))  # делаем запрос
    result = cursor.fetchall()
    conn.close()  # дисконектимся от базы данных
    return result


headings = sql_columns_names(2, 123, 'IO-61')[2::]
average = sql_average(2, 123, 'IO-61')[0]

print(headings, '\n', average)

x = range(len(average))
ax = plt.gca()
ax.bar(x, average)
ax.set_xticks(x)
ax.set_xticklabels(headings)
plt.show()
