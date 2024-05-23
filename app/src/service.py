
class Service:
    def __init__(self, name=None, category=None, duration=None, price=None, accepted_lvl=None):
        self._name = name or "Haircut"
        self._category = category or "basic"
        self._duration = duration or 60
        self._price = price or 500
        self._accepted_lvl = accepted_lvl or []

    def get_name(self):
        return self._name

    def get_category(self):
        return self._category

    def get_duration(self):
        return self._duration

    def get_price(self):
        return self._price
