import customtkinter as ctk

arr_1 = []
arr_2 = []
arr_3 = []



def button_admission():
    label = ctk.CTkLabel(app, text="e", fg_color="transparent").pack()

def combobox_menall(metall):
    arr_1.append(metall)
    print(arr_1)
    
def combobox_razmer(razmer):
    arr_2.append(razmer)
    print(arr_2)

def combobox_quantity(quantity):
    arr_3.append(quantity)
    print(arr_3)



app = ctk.CTk()

# характеристики окна программы
app.title("СИСТЕМА УЧЕТА МЕТАЛЛА В ПЦ")
app.geometry("800x500")

# добавление подписей
title_1 = ctk.CTkLabel(master=app, text = "ПРИХОД МЕТАЛЛА").pack()

# добавление кнопки
button = ctk.CTkButton(master=app, text="ЗАПИСАТЬ ПРИХОД", command=button_admission).pack()

combobox_metall = ctk.CTkComboBox(app, values=["УГОЛОК", "ЛИСТ", "ШВЕЛЛЕР"], command=combobox_menall).pack()
combobox_raxmer = ctk.CTkComboBox(app, values=["10", "20", "30"], command=combobox_razmer).pack()
entry_quantity = ctk.CTkEntry(app, placeholder_text="КОЛИЧЕСТВО, кг").pack()
e = entry_quantity.get()
print(e)







app.mainloop()