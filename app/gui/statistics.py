from tkinter import ttk, Label, Button
from app import barber_shop
import math

class StatisticsTab:
    def __init__(self, tab_control):
        self.frame = ttk.Frame(tab_control)
        self.frame.pack(expand=True, fill='both')
        self.setup_widgets()

    def fetch_statistics(self):
        barber_shop.simulate()

        revenue_by_barber = barber_shop.revenue_by_barber()
        revenue_barbershop = barber_shop.revenue_barbershop()
        revenue_by_barber_level = barber_shop.revenue_by_barber_level()
        average_time_wait_client = barber_shop.average_time_wait_client()
        random_clients, regular_clients = barber_shop.get_timeout_clients()
        earn_by_type_lvl = barber_shop.revenue_by_service_type()
        revenue_diff_non_standard = sum(
            v for k, v in earn_by_type_lvl.items() if k != 'non-standard') - earn_by_type_lvl.get('non-standard', 0)

        average_wait_time_formatted = self.format_time(average_time_wait_client * 60)

        statistics = {
            "total_revenue": f"Общая выручка: {revenue_barbershop} $",
            "revenue_by_barber": f"Выручка каждого парикмахера:\n" + "\n".join([f"{item} $" for item in revenue_by_barber.split()]),
            "revenue_by_level": "Выручка с разбивкой по уровню парикмахеров:\n" + "\n".join([f"{k}: {v} $" for k, v in revenue_by_barber_level.items()]),
            "average_wait_time": f"Среднее время ожидания клиента: {average_wait_time_formatted}",
            "unattended_clients": f"Клиенты ушедшие (рандомные/постоянные): {random_clients} / {regular_clients}",
            "revenue_by_service_type": (
                "Выручка с разбивкой по типам услуг:\n"
                f"  Базовая: {earn_by_type_lvl.get('basic', 0)} $\n"
                f"  Не стандартная: {earn_by_type_lvl.get('non-standard', 0)} $\n"
                f"  Стандартная: {earn_by_type_lvl.get('standard', 0)} $\n"
                f"  Сложная: {earn_by_type_lvl.get('complex', 0)} $"
            ),
            "revenue_diff_non_standard": (
                f"Разница в выручке между парикмахерами с нестандартными услугами и без: {abs(revenue_diff_non_standard)} $"
            )
        }

        return statistics

    def format_time(self, seconds):
        hours = math.floor(seconds / 3600)
        minutes = math.floor((seconds % 3600) / 60)
        seconds = seconds % 60
        return f"{hours} часов {minutes} минут {seconds:.0f} секунд"

    def update_statistics(self):
        stats = self.fetch_statistics()
        self.display_statistics(stats)

    def display_statistics(self, stats):
        for widget in self.frame.winfo_children():
            widget.destroy()

        for key, value in stats.items():
            Label(self.frame, text=value, font=('Arial', 12), anchor='w', justify='left').pack(pady=5, padx=10, anchor='w')

        Button(self.frame, text="Обновить статистику", command=self.update_statistics).pack(pady=10)

    def setup_widgets(self):
        Button(self.frame, text="Обновить статистику", command=self.update_statistics).pack(pady=10)
        return
        # self.update_statistics()
