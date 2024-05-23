import tkinter as tk
from tkinter import ttk, messagebox

from app import barber_shop


class ClientsTab:
    def __init__(self, tab_control):
        self.frame = ttk.Frame(tab_control)
        self.frame.pack(fill='both', expand=True)
        self.clients = []
        self.setup_widgets()

    def setup_widgets(self):
        self.tree = ttk.Treeview(self.frame, columns=(
            'desired_service',
            'is_regular',
            'max_time_wait',
            'preferred_barber',
            # 'timeout',
            # 'wait_time'
        ), show='headings')

        self.tree.heading('desired_service', text='Услуга')
        self.tree.heading('is_regular', text='Постоянный клиент')
        self.tree.heading('max_time_wait', text='Максимальное время ожидания')
        self.tree.heading('preferred_barber', text='Барбер')
        # self.tree.heading('timeout', text='timeout')
        # self.tree.heading('wait_time', text='Время ожидания')

        self.tree.column('desired_service', anchor='center')
        self.tree.column('is_regular', anchor='center')
        self.tree.column('max_time_wait', anchor='center')
        self.tree.column('preferred_barber', anchor='center')
        # self.tree.column('timeout', anchor='center')
        # self.tree.column('wait_time', anchor='center')
        self.tree.pack(side='left', fill='both', expand=True)

        scrollbar = ttk.Scrollbar(self.frame, orient='vertical', command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=scrollbar.set)

        input_frame = ttk.Frame(self.frame)
        input_frame.pack(side='top', fill='x', padx=20, pady=20)

        ttk.Label(input_frame, text="Услуги:").pack(pady=5)
        client_options = list(dict().fromkeys(service.get_name() for service in barber_shop.getServices()).keys())
        self.client_service_combobox = ttk.Combobox(input_frame, values=client_options)
        self.client_service_combobox.pack(pady=5)

        ttk.Label(input_frame, text="Время ожидания:").pack(pady=5)
        max_time_options = ["5", "10", "30", "60", "120"]
        self.max_time_wait_entry = ttk.Combobox(input_frame, values=max_time_options)
        self.max_time_wait_entry.pack(pady=5)

        ttk.Label(input_frame, text="Барбер:").pack(pady=5)
        service_name_obj = [service.get_name() for service in barber_shop.getBarbers()]
        service_name_obj.append("Не выбран")
        preferred_barber_options = list(dict().fromkeys(service_name_obj).keys())
        self.preferred_barber_entry = ttk.Combobox(input_frame, values=preferred_barber_options)
        self.preferred_barber_entry.pack(pady=5)

        # ttk.Label(input_frame, text="Постоянный клиент:").pack(pady=5)
        self.is_regular = True
        self.is_regular_start = tk.IntVar(value=1)
        ttk.Checkbutton(input_frame,
                        text="Постоянный клиент:",
                        variable=self.is_regular_start,
                        command=self.change_is_regular).pack(pady=10)

        ttk.Button(input_frame, text="Добавить клиента", command=self.add_clients).pack(pady=10)
        self.load_clients()

    def change_is_regular(self):
        self.is_regular = not self.is_regular

    def add_clients(self):
        service = self.client_service_combobox.get()
        is_regular = self.is_regular
        max_time_wait = self.max_time_wait_entry.get()
        preferred_barber = self.preferred_barber_entry.get()
        if preferred_barber and max_time_wait and service:
            self.tree.insert('', 'end', values=(service, "Да" if is_regular else "Нет", max_time_wait, preferred_barber))
            messagebox.showinfo("Успех", "Клиент добавлен успешно!")
        else:
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")

    def load_clients(self):
        for client in barber_shop.getClients():
            data = (
                client.desired_service.get_name(),
                "Да" if client.get_is_regular() else "Нет",
                client.get_max_time_wait(),
                client_service.get_name() if (client_service := client.get_preferred_barber()) else "Не выбран",
                # client.get_timeout(),
                # client.get_wait_time()
            )
            self.clients.append(data)
            self.tree.insert('', 'end', values=data)
