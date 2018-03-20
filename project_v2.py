from tkinter import *
# import sqlite3


class View:
    options_1 = ('1', '2', '3', '4', '5', '6')  # курсы
    options_2 = ('121', '122', '123', '124', '125')  # специальности
    options_121 = ('ІП-61', 'ІП-62', 'ІП-63', 'ІП-64', 'ІП-65')  # группы
    options_122 = ('ІС-61', 'ІС-62', 'ІС-63', 'ІС-64', 'ІС-65')
    options_123 = ('ІО-61', 'ІО-62', 'ІО-63', 'ІО-64', 'ІО-65')
    options_124 = ('ІК-61', 'ІК-62', 'ІК-63', 'ІК-64', 'ІК-65')
    options_125 = ('ІT-61', 'ІT-62', 'ІT-63', 'ІT-64', 'ІT-65')

    def __init__(self, master):
        # Настраиваем характеристика главного окна
        self.master = master
        master['bg'] = 'grey90'
        master.title('Аналіз Успішності Студентів ФІОТ')
        root.wm_geometry("%dx%d+%d+%d" % (800, 500, 225, 70))  # размер окна + расположение
        # надписи
        self.label_curs = Label(master, text="Курс").grid(row=1, column=3)
        self.label_spec = Label(self.master, text="Спеціальність ").grid(row=3, column=3)
        self.label_group = Label(master, text="Група").grid(row=5, column=3)
        # кнопочки
        self.my_button1 = Button(master, text=self.options_1[0], command=lambda: self.func_step1(1), width=5)
        self.my_button2 = Button(master, text=self.options_1[1], command=lambda: self.func_step1(2), width=5)
        self.my_button3 = Button(master, text=self.options_1[2], command=lambda: self.func_step1(3), width=5)
        self.my_button4 = Button(master, text=self.options_1[3], command=lambda: self.func_step1(4), width=5)
        self.my_button5 = Button(master, text=self.options_1[4], command=lambda: self.func_step1(5), width=5)
        self.my_button6 = Button(master, text=self.options_1[5], command=lambda: self.func_step1(6), width=5)
        self.my_button1.grid(row=2, column=1)
        self.my_button2.grid(row=2, column=2)
        self.my_button3.grid(row=2, column=3)
        self.my_button4.grid(row=2, column=4)
        self.my_button5.grid(row=2, column=6)
        self.my_button6.grid(row=2, column=7)
        # технические лейблы
        self.label_technical_1 = Label(master, width=40, height=10)  # для пустого пространства слева и сверху
        self.label_technical_1.grid(row=0, column=0)
        self.label_technical_2 = Label(master, width=10, height=5)  # для пустого пространства между кнопкой1 и кн2
        self.label_technical_2.grid(row=3, column=0, rowspan=2)
        self.label_technical_3 = Label(master, width=40, height=2)  # для пустого пространства перед Кнопкой сверху
        self.label_technical_3.grid(row=6, column=0)

        self.go_button = Button(master, text='Пошук', command=self.the_function, relief=GROOVE, overrelief=RIDGE, bd=2)
        self.go_button.grid(row=8, column=3)

        self.label_result = Label(self.master)
        self.label_result.grid(row=7, column=2, columnspan=5)

    # Функции первого шага
    def func_step1(self, curs):
        """ Функция, которая вызывается при выборе курса
        Создает и размещает кнопки c нужными специальностями """
        self.my_button1 = Button(self.master, text=self.options_2[0],
                                 command=lambda: self.func_step2(self.options_121, curs, self.options_2[0]), width=5)
        self.my_button2 = Button(self.master, text=self.options_2[1],
                                 command=lambda: self.func_step2(self.options_122, curs, self.options_2[1]), width=5)
        self.my_button3 = Button(self.master, text=self.options_2[2],
                                 command=lambda: self.func_step2(self.options_123, curs, self.options_2[2]), width=5)
        self.my_button4 = Button(self.master, text=self.options_2[3],
                                 command=lambda: self.func_step2(self.options_124, curs, self.options_2[3]), width=5)
        self.my_button5 = Button(self.master, text=self.options_2[4],
                                 command=lambda: self.func_step2(self.options_125, curs, self.options_2[4]), width=5)

        self.my_button1.grid(row=4, column=1)
        self.my_button2.grid(row=4, column=2)
        self.my_button3.grid(row=4, column=3)
        self.my_button4.grid(row=4, column=4)
        self.my_button5.grid(row=4, column=6)

    # Функции второго шага
    def func_step2(self, values, curs, spec):  # параметр values - это список/котреж групп. ex: ('ІО-61', 'ІО-62'..)
        """ Функция, которая вызывается, при выборе специальности
        Создает и размещает кнопки с группами выбраной специальности"""
        self.my_button1 = Button(self.master, text=values[0], command=lambda: self.chose_group(curs, spec, 61), width=5)
        self.my_button2 = Button(self.master, text=values[1], command=lambda: self.chose_group(curs, spec, 62), width=5)
        self.my_button3 = Button(self.master, text=values[2], command=lambda: self.chose_group(curs, spec, 63), width=5)
        self.my_button4 = Button(self.master, text=values[3], command=lambda: self.chose_group(curs, spec, 64), width=5)
        self.my_button5 = Button(self.master, text=values[4], command=lambda: self.chose_group(curs, spec, 65), width=5)
        self.my_button1.grid(row=6, column=1)
        self.my_button2.grid(row=6, column=2)
        self.my_button3.grid(row=6, column=3)
        self.my_button4.grid(row=6, column=4)
        self.my_button5.grid(row=6, column=6)

    # Функции третьего шага

    def chose_group(self, curs, spec, number):
        """Функция, которая вызывается при нажатии на <> группу"""
        self.label_result['text'] = 'Курс: {}. Спеціальність {}. Група {}.'.format(curs, spec, number)
        print('Ви вибрали: {} курс {} спеціальність {} група'.format(curs, spec, number))

        # conn = sqlite3.connect('my_group.db')

        # cursor1 = conn.execute('SELECT * FROM io{}'.format(number))
        # result1 = cursor1.fetchall()

        # for i in result1:
        #    print(i)

        # conn.close()

    @staticmethod
    def the_function():
        """Функция, которая вызывается при нажатии на <ПОШУК> """
        print('Hey, billy')
        pass


if __name__ == '__main__':
    root = Tk()
    my_gui = View(root)
    root.mainloop()
