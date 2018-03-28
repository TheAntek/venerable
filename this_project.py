from tkinter import *
from tkinter.ttk import Treeview, Style, Button as Button_ttk
import sqlite3


def sql_table(curs, spec, group):
    """Есть папки курсов. В них есть базы данных специальностей этого курса. В каждой бд есть таблицы групп
    Например: curs_2/spec_123.db (Таблица io61 в этой базе данных)"""
    conn = sqlite3.connect('database\\curs_{}\\spec{}_v2.db'.format(curs, spec))  # конектимся к базе данных
    cursor = conn.execute('SELECT * FROM {}'.format(group.replace('-', '').lower()))  # делаем запрос. IO-61 --> io61
    result = cursor.fetchall()  # в переменную присваиваем результата запроса

    print(result)
    conn.close()  # дисконектимся от базы данных

    return result


def sql_columns_names(curs, spec, group):
    """Возвращает названия столбцов"""
    conn = sqlite3.connect('database\\Curs_{}\\spec{}_v2.db'.format(curs, spec))  # конектимся к базе данных
    cursor = conn.execute('SELECT * FROM {}'.format(group.replace('-', '').lower()))  # делаем запрос
    columns_names = [desc[0] for desc in cursor.description]  # получаем название стобцов

    print(columns_names)
    conn.close()  # дисконектимся от базы данных

    return columns_names


class View2:
    """ Окно, которое открывается при нажатии на 'Вибрати' """
    def __init__(self, master, curs, spec, group, headings, rows):
        self.master = master
        self.curs = curs
        self.spec = spec
        self.group = group
        self.headings = headings
        self.rows = rows
        master.wm_geometry("%dx%d+%d+%d" % (800, 500, 250, 95))

        # style = Style()
        # style.configure(".", font=('Helvetica', 8))
        # style.configure("Treeview", foreground='red')
        # style.configure("Treeview.Heading", foreground='green')

        self.my_table = Treeview(master, show='headings', height=19)  # создаем таблицу
        self.fill_table()  # заполняем таблицу
        self.my_table.grid(row=1, column=0)  # выводим таблицу

        self.label_info = Label(master, text='Курс: {}\nСпеціальність: {}\nГрупа: {}'.format(curs, spec, group))
        self.label_info.grid(row=0, column=0)

        self.quitButton = Button_ttk(master, text='Закрити', width='20', command=self.close_window, style='Fun.TButton')
        self.quitButton.grid(row=2, column=0)

    def fill_table(self):
        """ Работаем с таблицой """
        self.my_table['columns'] = self.headings  # в 'столбцы' присваиваем переменную

        for head in self.headings:
            """ Создаем столбцы. Если это стоблец П.И.Б. - делаем ширину больше """
            if head == 'full_name':
                self.my_table.heading(head, text=head, anchor=CENTER)
                self.my_table.column(head, anchor=CENTER, width=193)
            else:
                self.my_table.heading(head, text=head, anchor=CENTER)
                self.my_table.column(head, anchor=CENTER, width=55)

        for row in self.rows:
            self.my_table.insert('', END, values=row)  # вставляем в каждую строку таблицы нужный кортеж значений

    def close_window(self):
        """ Устрой дестрой """
        self.master.destroy()


class View:
    """ Главное окно """
    options_2 = ('121', '122', '123', '124', '125')  # специальности
    # все группы каждой специальности
    options_121 = (('ІП-71', 'ІП-72', 'ІП-73', 'ІП-74', 'ІП-75'), ('ІП-61', 'ІП-62', 'ІП-63', 'ІП-64', 'ІП-65'),
                   ('ІП-51', 'ІП-52', 'ІП-53', 'ІП-54', 'ІП-55'), ('ІП-41', 'ІП-42', 'ІП-43', 'ІП-44', 'ІП-45'))

    options_122 = (('ІС-71', 'ІС-72', 'ІС-73', 'ІС-74', 'ІС-75'), ('ІС-61', 'ІС-62', 'ІС-63', 'ІС-64', 'ІС-65'),
                   ('ІС-51', 'ІС-52', 'ІС-53', 'ІС-54', 'ІС-55'), ('ІС-41', 'ІС-42', 'ІС-43', 'ІС-44', 'ІС-45'))

    options_123 = (('ІО-71', 'ІО-72', 'ІО-73', 'ІО-74', 'ІО-75'), ('IO-61', 'IO-62', 'IO-63', 'IO-64', 'IO-65'),
                   ('ІО-51', 'ІО-52', 'ІО-53', 'ІО-54', 'ІО-55'), ('ІО-41', 'ІО-42', 'ІО-43', 'ІО-44', 'ІО-45'))

    options_124 = (('ІК-71', 'ІК-72', 'ІК-73', 'ІК-74', 'ІК-75'), ('ІК-61', 'ІК-62', 'ІК-63', 'ІК-64', 'ІК-65'),
                   ('ІК-51', 'ІК-52', 'ІК-53', 'ІК-54', 'ІК-55'), ('ІК-41', 'ІК-42', 'ІК-43', 'ІК-44', 'ІК-45'))

    options_125 = (('ІT-71', 'ІT-72', 'ІT-73', 'ІT-74', 'ІT-75'), ('ІT-61', 'ІT-62', 'ІT-63', 'ІT-64', 'ІT-65'),
                   ('ІT-51', 'ІT-52', 'ІT-53', 'ІT-54', 'ІT-55'), ('ІT-41', 'ІT-42', 'ІT-43', 'ІT-44', 'ІT-45'))

    def __init__(self, master):
        # Настраиваем характеристика главного окна
        self.master = master
        master['bg'] = 'grey90'
        master.title('Аналіз Успішності Студентів ФІОТ')
        master.wm_geometry("%dx%d+%d+%d" % (800, 500, 225, 70))  # размер окна + расположение
        # надписи
        self.label_curs = Label(master, text="Курс").grid(row=1, column=3)
        self.label_spec = Label(self.master, text="Спеціальність ").grid(row=3, column=3)
        self.label_group = Label(master, text="Група").grid(row=5, column=3)
        # кнопочки (выбираем курс)
        self.my_button1 = Button(master, text='1', command=lambda: self.func_step1(1), width=5)
        self.my_button2 = Button(master, text='2', command=lambda: self.func_step1(2), width=5)
        self.my_button3 = Button(master, text='3', command=lambda: self.func_step1(3), width=5)
        self.my_button4 = Button(master, text='4', command=lambda: self.func_step1(4), width=5)
        self.my_button5 = Button(master)
        self.my_button1.grid(row=2, column=1)
        self.my_button2.grid(row=2, column=2)
        self.my_button3.grid(row=2, column=3)
        self.my_button4.grid(row=2, column=4)

        # технические лейблы
        self.label_technical_1 = Label(master, width=40, height=10)  # для пустого пространства слева и сверху
        self.label_technical_1.grid(row=0, column=0)
        self.label_technical_2 = Label(master, width=10, height=5)  # для пустого пространства между кнопкой1 и кн2
        self.label_technical_2.grid(row=3, column=0, rowspan=2)
        self.label_technical_3 = Label(master, width=40, height=2)  # для пустого пространства перед Кнопкой сверху
        self.label_technical_3.grid(row=6, column=0)

        # лейбл, который отображает, что вы выбрали в первом окне
        self.label_result = Label(self.master)
        self.label_result.grid(row=7, column=2, columnspan=5)

        self.go_button = None  # кнопка 'вибрати'
        self.new_window = None  # второе окно делаем
        self.app = None  # второе окно

    # Функции первого шага
    def func_step1(self, curs):
        """ Функция, которая вызывается при выборе курса
        Создает и размещает кнопки c нужными специальностями """
        self.my_button1 = Button(self.master, text=self.options_2[0], width=5,
                                 command=lambda: self.func_step2(self.options_121[curs-1], curs, self.options_2[0]))
        self.my_button2 = Button(self.master, text=self.options_2[1], width=5,
                                 command=lambda: self.func_step2(self.options_122[curs-1], curs, self.options_2[1]))
        self.my_button3 = Button(self.master, text=self.options_2[2], width=5,
                                 command=lambda: self.func_step2(self.options_123[curs-1], curs, self.options_2[2]))
        self.my_button4 = Button(self.master, text=self.options_2[3], width=5,
                                 command=lambda: self.func_step2(self.options_124[curs-1], curs, self.options_2[3]))
        self.my_button5 = Button(self.master, text=self.options_2[4], width=5,
                                 command=lambda: self.func_step2(self.options_125[curs-1], curs, self.options_2[4]))

        self.my_button1.grid(row=4, column=1)
        self.my_button2.grid(row=4, column=2)
        self.my_button3.grid(row=4, column=3)
        self.my_button4.grid(row=4, column=4)
        self.my_button5.grid(row=4, column=6)

    # Функции второго шага
    def func_step2(self, values, curs, spec):  # параметр values - это список/котреж групп. ex: ('ІО-61', 'ІО-62'..)
        """ Функция, которая вызывается, при выборе специальности
        Создает и размещает кнопки с группами выбраной специальности"""
        self.my_button1 = Button(self.master, text=values[0], width=5,
                                 command=lambda: self.chose_group(curs, spec, values[0]))
        self.my_button2 = Button(self.master, text=values[1], width=5,
                                 command=lambda: self.chose_group(curs, spec, values[1]))
        self.my_button3 = Button(self.master, text=values[2], width=5,
                                 command=lambda: self.chose_group(curs, spec, values[2]))
        self.my_button4 = Button(self.master, text=values[3], width=5,
                                 command=lambda: self.chose_group(curs, spec, values[3]))
        self.my_button5 = Button(self.master, text=values[4], width=5,
                                 command=lambda: self.chose_group(curs, spec, values[4]))
        self.my_button1.grid(row=6, column=1)
        self.my_button2.grid(row=6, column=2)
        self.my_button3.grid(row=6, column=3)
        self.my_button4.grid(row=6, column=4)
        self.my_button5.grid(row=6, column=6)

    # Функции третьего шага
    def chose_group(self, curs, spec, group):
        """Функция, которая вызывается при нажатии на <> группу"""
        self.label_result['text'] = 'Курс: {}. Спеціальність {}. Група {}.'.format(curs, spec, group)
        self.go_button = Button(self.master, text='Вибрати', relief=GROOVE, overrelief=RIDGE, bd=2,
                                command=lambda: self.the_function(curs, spec, group))

        self.go_button.grid(row=8, column=3)
        print('Ви вибрали: {} курс {} спеціальність {} група'.format(curs, spec, group))

    def the_function(self, curs, spec, group):
        """Функция, которая вызывается при нажатии на <Вибрати> """
        students = sql_table(curs, spec, group)  # students - список кортежей. ex: [('1', '2'), ('3', '4')..]
        columns = sql_columns_names(curs, spec, group)  # columns - список названий столбцов

        # Создаем новое окно
        self.new_window = Toplevel(self.master)
        self.app = View2(self.new_window, curs, spec, group, columns, students)


if __name__ == '__main__':
    root = Tk()
    my_gui = View(root)
    root.mainloop()
