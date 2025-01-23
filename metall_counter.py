import customtkinter as ctk

def button_admission():
    print("Запись в БД прихода")

def butto_consuption():
    print("Запись в БД расхода")

def butto_register():
    print("Провести Транзакцию")



app = ctk.CTk()

# характеристики окна программы
app.title("СИСТЕМА УЧЕТА МЕТАЛЛА В ПЦ")
app.geometry("1000x800")

# добавление подписей
title_1 = ctk.CTkLabel(app, text = "ПРИХОД МЕТАЛЛА")
title_1.grid(row=0, column=0, padx=20, pady=20)
title_2 = ctk.CTkLabel(app, text = "РАСХОД МЕТАЛЛА")
title_2.grid(row=2, column=0, padx=20, pady=20)

# добавление кнопки
button = ctk.CTkButton(app, text="ПРИХОД МЕТАЛЛА", command = button_admission)
button.grid(row=1, column=0, padx=20, pady=10)
button = ctk.CTkButton(app, text="РАСХОД МЕТАЛЛА", command = butto_consuption)
button.grid(row=3, column=0, padx=20, pady=10)
button = ctk.CTkButton(app, text="ПРОВЕСТИ ТРАНЗАКЦИЮ", command = butto_consuption)
button.grid(row=4, column=0, padx=20, pady=10)



# добавление поля ввода мастера
entry_1 = ctk.CTkEntry(app, placeholder_text="Фамилия мастер")
entry_1.grid(row=5, column=0, padx=20, pady=10)




app.mainloop()