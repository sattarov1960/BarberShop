import tkinter as tk
from tkinter import ttk, messagebox

from app import barber_shop


class BarbersTab:
    def __init__(self, tab_control):
        self.frame = ttk.Frame(tab_control)
        self.frame.pack(fill='both', expand=True)
        self.barbers = []
        self.setup_widgets()

    def setup_widgets(self):
        self.tree = ttk.Treeview(self.frame, columns=('lvl', 'services', 'name'), show='headings')
        self.tree.heading('lvl', text='Уровень')
        self.tree.heading('services', text='Услуги')
        self.tree.heading('name', text='Имя')
        self.tree.column('lvl', anchor='center')
        self.tree.column('services', anchor='center')
        self.tree.column('name', anchor='center')
        self.tree.pack(side='left', fill='both', expand=True)

        scrollbar = ttk.Scrollbar(self.frame, orient='vertical', command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=scrollbar.set)

        input_frame = ttk.Frame(self.frame)
        input_frame.pack(side='top', fill='x', padx=20, pady=20)

        ttk.Label(input_frame, text="Уровень:").pack(pady=5)
        service_options = ['master', 'experienced', 'beginner']
        self.barber_service_combobox = ttk.Combobox(input_frame, values=service_options)
        self.barber_service_combobox.pack(pady=5)

        ttk.Label(input_frame, text="Услуги:").pack(pady=5)
        service_options = list(set(service.get_name() for service in barber_shop.getServices()))
        self.services_entry = ttk.Combobox(input_frame, values=service_options)
        self.services_entry.pack(pady=5)

        ttk.Label(input_frame, text="Имя:").pack(pady=5)
        self.name_entry = ttk.Entry(input_frame)
        self.name_entry.pack(pady=5)

        ttk.Button(input_frame, text="Добавить барбера", command=self.add_barber).pack(pady=10)
        self.load_barbers()

    def add_barber(self):
        lvl = self.barber_service_combobox.get()
        service = self.services_entry.get()
        name = self.name_entry.get()
        if lvl and service and name:
            self.tree.insert('', 'end', values=(lvl, service, name))
            self.barber_service_combobox.delete(0, tk.END)
            self.services_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)
            messagebox.showinfo("Успех", "Барбер добавлен успешно!")
        else:
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")

    def load_barbers(self):
        for barber in barber_shop.getBarbers():
            data = (barber.get_level(),
                    "; ".join([service.get_name() for service in barber.get_services()]),
                    barber.get_name())
            self.barbers.append(data)
            self.tree.insert('', 'end', values=data)
