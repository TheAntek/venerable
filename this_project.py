from tkinter import *
from tkinter.ttk import Treeview, Style, Button as Button_ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import arange
import sqlite3


def sql_select(curs, spec, group):
    """Есть папки курсов. В них есть базы данных специальностей этого курса. В каждой бд есть таблицы групп
    Например: curs_2/spec_123.db (Таблица io61 в этой базе данных)"""
    conn = sqlite3.connect('database\\curs_{}\\spec{}_v2.db'.format(curs, spec))  # конектимся к базе данных
    cursor = conn.execute('SELECT * FROM {} ORDER BY id;'.format(group.replace('-', '').lower()))  # делаем запрос. IO-61 --> io61
    result = cursor.fetchall()  # в переменную присваиваем результата запроса
    # print(result)
    conn.close()  # дисконектимся от базы данных

    return result


def sql_columns_names(curs, spec, group):
    """Возвращает названия столбцов"""
    conn = sqlite3.connect('database\\Curs_{}\\spec{}_v2.db'.format(curs, spec))  # конектимся к базе данных
    cursor = conn.execute('SELECT * FROM {};'.format(group.replace('-', '').lower()))  # делаем запрос
    columns_names = [desc[0] for desc in cursor.description]  # получаем название стобцов
    # print(columns_names)
    conn.close()  # дисконектимся от базы данных

    return columns_names


def sql_delete(curs, spec, group, number):
    """ Удаление студента с базы данных """
    conn = sqlite3.connect('database\\curs_{}\\spec{}_v2.db'.format(curs, spec))
    conn.execute('DELETE FROM {} WHERE id = {};'.format(group.replace('-', '').lower(), number))
    conn.commit()
    # print('deleted')
    conn.close()


def sql_insert(curs, spec, group, info):
    """ Добавление студента в базу данных """
    conn = sqlite3.connect('database\\curs_{}\\spec{}_v2.db'.format(curs, spec))
    # print('INSERT INTO {} VALUES (?, ?, ?);'.format(group.replace('-', '').lower(), number, name, marks))
    conn.execute('INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'.
                 format(group.replace('-', '').lower()), info)
    conn.commit()
    # print('inserted')
    conn.close()


def sql_average(curs, spec, group):
    conn = sqlite3.connect('database\\Curs_{}\\spec{}_v2.db'.format(curs, spec))  # конектимся к базе данных
    cursor = conn.execute('SELECT AVG(mark_1), AVG(mark_2), AVG(mark_3), AVG(mark_4), AVG(mark_5), AVG(mark_6),'
                          ' AVG(mark_7), AVG(mark_8), AVG(mark_9), AVG(mark_10) FROM {};'
                          .format(group.replace('-', '').lower()))  # делаем запрос
    result = cursor.fetchall()
    print(result)
    conn.close()  # дисконектимся от базы данных
    return result


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
        # master.overrideredirect(1)
        # master.geometry("%dx%d+0+0" % (root.winfo_screenwidth(), root.winfo_screenheight()))
        # master['bg'] = 'grey90'
        master.title('Аналіз Успішності Студентів ФІОТ')
        master.wm_geometry("%dx%d+%d+%d" % (800, 500, 225, 70))  # размер окна + расположение
        # надписи
        self.label_curs = Label(master, text="Курс").grid(row=1, column=3)
        self.label_spec = Label(self.master, text="Спеціальність ").grid(row=3, column=3)
        self.label_group = Label(master, text="Група").grid(row=5, column=3)
        # кнопочки (выбираем курс)
        self.my_button1 = Button_ttk(master, text='1', command=lambda: self.func_step1(1), width=5)
        self.my_button2 = Button_ttk(master, text='2', command=lambda: self.func_step1(2), width=5)
        self.my_button3 = Button_ttk(master, text='3', command=lambda: self.func_step1(3), width=5)
        self.my_button4 = Button_ttk(master, text='4', command=lambda: self.func_step1(4), width=5)
        self.my_button5 = Button_ttk(master)
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
        self.my_button1 = Button_ttk(self.master, text=self.options_2[0], width=5,
                                     command=lambda: self.func_step2(self.options_121[curs-1], curs, self.options_2[0]))
        self.my_button2 = Button_ttk(self.master, text=self.options_2[1], width=5,
                                     command=lambda: self.func_step2(self.options_122[curs-1], curs, self.options_2[1]))
        self.my_button3 = Button_ttk(self.master, text=self.options_2[2], width=5,
                                     command=lambda: self.func_step2(self.options_123[curs-1], curs, self.options_2[2]))
        self.my_button4 = Button_ttk(self.master, text=self.options_2[3], width=5,
                                     command=lambda: self.func_step2(self.options_124[curs-1], curs, self.options_2[3]))
        self.my_button5 = Button_ttk(self.master, text=self.options_2[4], width=5,
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
        self.my_button1 = Button_ttk(self.master, text=values[0], width=5,
                                     command=lambda: self.chose_group(curs, spec, values[0]))
        self.my_button2 = Button_ttk(self.master, text=values[1], width=5,
                                     command=lambda: self.chose_group(curs, spec, values[1]))
        self.my_button3 = Button_ttk(self.master, text=values[2], width=5,
                                     command=lambda: self.chose_group(curs, spec, values[2]))
        self.my_button4 = Button_ttk(self.master, text=values[3], width=5,
                                     command=lambda: self.chose_group(curs, spec, values[3]))
        self.my_button5 = Button_ttk(self.master, text=values[4], width=5,
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
        self.go_button = Button_ttk(self.master, text='Вибрати', command=lambda: self.the_function(curs, spec, group))

        self.go_button.grid(row=8, column=3)
        # print('Ви вибрали: {} курс {} спеціальність {} група'.format(curs, spec, group))

    def the_function(self, curs, spec, group):
        """Функция, которая вызывается при нажатии на <Вибрати> """
        students = sql_select(curs, spec, group)  # students - список кортежей. ex: [('1', '2'), ('3', '4')..]
        columns = sql_columns_names(curs, spec, group)  # columns - список названий столбцов

        # Создаем новое окно
        self.new_window = Toplevel(self.master)
        self.app = View2(self.new_window, curs, spec, group, columns, students)


class View2:
    """ Окно, которое открывается при нажатии на 'Вибрати' """
    def __init__(self, master, curs, spec, group, headings, rows):
        self.master = master
        self.curs = curs
        self.spec = spec
        self.group = group
        self.headings = headings
        self.rows = rows
        self.average = None
        master.wm_geometry("%dx%d+%d+%d" % (800, 500, 250, 95))

        # style = Style()
        # style.configure(".", font=('Helvetica', 8))
        # style.configure("Treeview", foreground='red')
        # style.configure("Treeview.Heading", foreground='green')

        self.my_table = Treeview(master, show='headings', height=19)  # создаем таблицу
        self.fill_table()  # заполняем таблицу
        self.my_table.grid(row=1, column=0, columnspan=3)  # выводим таблицу

        self.label_info = Label(master, text='Курс: {}\nСпеціальність: {}\nГрупа: {}'.format(curs, spec, group))
        self.label_info.grid(row=0, column=0)

        self.eButton = Button_ttk(master, text='Редагувати таблицю', width=20, command=self.edit)
        self.eButton.grid(row=2, column=0)

        self.updateButton = Button_ttk(master, text='Оновити таблицю', width=20, command=self.update)
        self.updateButton.grid(row=2, column=1)

        self.button_stat = Button_ttk(master, text='Статистика', width=20, command=self.stats)
        self.button_stat.grid(row=2, column=2)

        self.new_window = None
        self.app = None

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

    def edit(self):
        self.new_window = Toplevel(self.master)
        self.app = View3(self.new_window, self.curs, self.spec, self.group)

    def update(self):
        self.rows = sql_select(self.curs, self.spec, self.group)
        self.headings = sql_columns_names(self.curs, self.spec, self.group)

        self.my_table = Treeview(self.master, show='headings', height=19)
        self.fill_table()  # заполняем таблицу
        self.my_table.grid(row=1, column=0, columnspan=3)  # выводим таблицу

    def stats(self):
        self.headings = sql_columns_names(self.curs, self.spec, self.group)[2::]
        self.average = sql_average(self.curs, self.spec, self.group)[0]
        self.new_window = Toplevel(self.master)
        self.app = View4(self.new_window, self.headings, self.average, self.group)


class View3:
    def __init__(self, master, curs, spec, group):
        self.master = master
        self.curs = curs
        self.spec = spec
        self.group = group
        self.marks = []
        self.counter = 2
        self.headings = sql_columns_names(self.curs, self.spec, self.group)
        master.wm_geometry("%dx%d+%d+%d" % (400, 300, 800, 200))

        # Функционал для добавления значения (labels, entries, buttons)
        self.label_caption = Label(master, text='Запис студента в базу даних')
        self.label_caption.grid(row=0, column=0, columnspan=2)

        self.label_create_1 = Label(master, text='ПІБ')
        self.label_create_1.grid(row=1, column=0)
        self.entry_create_1 = Entry(master, width=15)
        self.entry_create_1.grid(row=1, column=1)

        self.label_create_2 = Label(master, text='id')
        self.label_create_2.grid(row=2, column=0)
        self.entry_create_2 = Entry(master, width=3)
        self.entry_create_2.grid(row=2, column=1)

        self.label_create_3 = Label(master, text=self.headings[self.counter])
        self.label_create_3.grid(row=3, column=0)
        self.entry_create_3 = Entry(master, width=3)
        self.entry_create_3.grid(row=3, column=1)

        self.button_create_add = Button_ttk(master, text='Ок', width=3, command=self.add_mark)
        self.button_create_add.grid(row=3, column=2)

        self.button_create_final = Button_ttk(master, text='Додати', width=25, command=self.create)
        self.button_create_final.grid(row=4, column=0, columnspan=2)

        self.label_create_0 = Label(master, text='Оцінки:')

        # Функционал для удаления значения (labels, entries, buttons)
        self.teh = Label(master)
        self.teh.grid(row=6, column=0)

        self.label_caption_delete = Label(master, text='Видалення студента з бази даних')
        self.label_caption_delete.grid(row=10, column=0, columnspan=2)

        self.label_delete = Label(master, text='Вкажіть id студента')
        self.label_delete.grid(row=11, column=0)

        self.entry_delete = Entry(master, width=3)
        self.entry_delete.grid(row=11, column=1)

        self.button_delete = Button_ttk(master, text='Видалити', width=25, command=self.delete)
        self.button_delete.grid(row=12, column=0, columnspan=2)

    def add_mark(self):
        self.counter += 1
        self.marks.append(self.entry_create_3.get())
        print(self.marks)
        self.label_create_3.destroy()
        self.entry_create_3.destroy()
        try:
            self.label_create_3 = Label(self.master, text=self.headings[self.counter])
        except IndexError:
            self.label_create_3.destroy()
            self.entry_create_3.destroy()
            self.button_create_add.destroy()
            self.label_create_0.grid(row=3, column=0)
            self.label_create_3 = Label(self.master, text=self.marks)
            self.label_create_3.grid(row=3, column=1, columnspan=2)
        else:
            self.label_create_3.grid(row=3, column=0)
            self.label_create_3.grid(row=3, column=0)
            self.entry_create_3 = Entry(self.master, width=3)
            self.entry_create_3.grid(row=3, column=1)

    def delete(self):
        print('deleting')
        student_id = self.entry_delete.get()  # получаем id, которое ввел пользователь
        sql_delete(self.curs, self.spec, self.group, student_id)  # вызываем функцию, которая удаляет студента по id

    def create(self):
        name = self.entry_create_1.get()
        number = self.entry_create_2.get()
        info = self.marks  # строка. пример: '90 95 65 70 87 100..'

        info.insert(0, name)  # в начало списка вставляем ФИО студента
        info.insert(0, number)  # также в начало вставляем номер студента
        print(info)  # переменная info выглядит след. образом: [id, 'Full Name', 90, 65, 70 ...]

        sql_insert(self.curs, self.spec, self.group, info)


class View4:
    """ Окно, где размещается диаграмма """
    def __init__(self, master, headings, average, group):
        self.master = master
        self.headings = headings
        self.average = average
        self.group = group
        master.wm_geometry("%dx%d+%d+%d" % (600, 450, 450, 120))

        self.fig = self.diagram()
        canvas = FigureCanvasTkAgg(self.fig, master)
        canvas.show()
        canvas.get_tk_widget().pack()

    def diagram(self):
        """ Построение гистрограммы """
        self.headings = sorted(self.headings)  # для коректного отображения чисел на гистограмме
        print(self.headings, '\n', self.average)
        num = arange(1, len(self.headings) + 1)  # список значений оси х

        figure = Figure()
        figure.suptitle('Успішніть студентів групи {}\nСередній бал: {}'.
                        format(self.group, sum(self.average)/len(self.average)))  # название графика (сверху)

        ax = figure.add_subplot(111)  # создаем полотно
        ax.bar(self.headings, self.average)  # гистограмма с значениями х и у
        figure.autofmt_xdate(bottom=0.2, rotation=50)  # формат подписей снизу

        for x, y in zip(num, self.average):
            ax.text(x - 1.35, y - 5, '%.1f' % y, color='white')  # подписываем каждый столбец

        return figure


if __name__ == '__main__':
    root = Tk()
    my_gui = View(root)
    root.mainloop()
