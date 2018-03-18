from tkinter import *
import xlrd

main_window = Tk()
main_window.title('Аналіз Успішності Студентів')
main_window.geometry('370x180')


# то что отображается изначально на выпадающих списках:
fct = StringVar(main_window)
fct.set("фіот")

crs = StringVar(main_window)
crs.set("1")

spc = StringVar(main_window)
spc.set("121")

our_excel_file = xlrd.open_workbook('./test.xlsx')
sheet = our_excel_file.sheet_by_index(0)

# dict = {'Факультет': 1, 'dictionary': 2}
my_list = []
final_list = []


def her():

    chosen_fct = 'text:' + "'" + str(fct.get()) + "'"
    chosen_crs = 'number:' + str(crs.get()) + ".0"
    chosen_spc = 'number:' + str(spc.get()) + ".0"

    print(chosen_crs, chosen_fct, chosen_spc)

    for i in range(sheet.nrows-16, sheet.nrows):

        if str(sheet.row(i)[9]) == chosen_fct:
            my_list.append({'имя фамилия': (sheet.row(i)[5]), 'Факультет': (sheet.row(i)[9]),
                            'курс': (sheet.row(i)[10]), 'специальность': (sheet.row(i)[11])})

    for i in range(len(my_list)):
        if (str(my_list[i]['курс']) == chosen_crs) and (str(my_list[i]['специальность']) == chosen_spc):
            final_list.append(my_list[i])

    print(my_list)
    for j in final_list:
        print(str(j))

    my_list.clear()
    final_list.clear()


# списки и текстовые поля:
f = Label(main_window, height=1, width=10, font='Arial 14', text='Факультет')
f.grid(row=0, column=0)

Faculty = OptionMenu(main_window, fct, "фіот", "іпса", "теф")
Faculty.grid(row=1, column=0)

c = Label(main_window, height=1, width=10, font='Arial 14', text='Курс')
c.grid(row=0, column=1)

Course = OptionMenu(main_window, crs, "1", "2", "3", "4", "5", "6")
Course.grid(row=1, column=1)

s = Label(main_window, height=1, width=10, font='Arial 14', text='Спеціалізація')
s.grid(row=0, column=2)

Specialization = OptionMenu(main_window, spc, "121", "122", "123", "124")
Specialization.grid(row=1, column=2)

go = Button(main_window, text='Пошук', command=her, width=10, bg='lime', fg='black', font='arial 10')
go.grid(row=3, column=1)

label_teh = Label(main_window, height=3, width=10, font='Arial 14')
label_teh.grid(row=2, column=0)

main_window.mainloop()
