import matplotlib.pyplot as plt
import sqlite3
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *


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


def my_figure():
    # headings = sql_columns_names(2, 123, 'IO-61')[2::]
    average = sql_average(2, 123, 'IO-61')[0]
    headings = sorted(['eng', 'ipz', 'oop', 'mat', 'mo', 'okk', 'amo', 'fp', 'uk', 'eco'])
    n = [1,2,3,4,5,6,7,8,9,10]
    print(headings, '\n', average)

    figure = Figure()
    ax = figure.add_subplot(111)
    ax.bar(headings, average)
    for x, y in zip(n, average):
        ax.text(x-1.35, y-5, '%.1f' % y, color='white')
    figure.autofmt_xdate(bottom=0.2, rotation=50)
    return figure

    # x = range(len(average))
    # ax = plt.gca()
    # ax.bar(x, average)
    # ax.set_xticks(x)
    # ax.set_xticklabels(headings)
    # plt.show()


root = Tk()
fig = my_figure()
canvas = FigureCanvasTkAgg(fig, root)
canvas.show()
canvas.get_tk_widget().pack()

root.mainloop()
