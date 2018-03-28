# С этого файла работаем с нашими базами данных
import sqlite3

conn = sqlite3.connect('database\\curs_2\\spec123_v2.db')

for i in range(10, 35):

    conn.execute('INSERT INTO io61 (id, full_name, mark_1, mark_2, mark_3, mark_4, mark_5, mark_6,  mark_7, mark_8, mark_9, mark_10)'
                          'VALUES ({}, "СреднееИмя И. П.", 95, 100, 60, 75, 90, 90, 90, 90, 90, 60);'.format(i))

conn.commit()

conn.close()
