
class Client:
    def __init__(self, desired_service, is_regular, max_time_wait, preferred_barber=None):
        self.desired_service = desired_service
        self.wait_time = 0
        self.is_regular = is_regular
        self.preferred_barber = preferred_barber
        self.max_time_wait = max_time_wait
        self.timeout = False

    def get_desired_service(self):
        return self.desired_service

    def get_wait_time(self):
        return self.wait_time

    def get_is_regular(self):
        return self.is_regular

    def get_preferred_barber(self):
        return self.preferred_barber

    def get_max_time_wait(self):
        return self.max_time_wait

    def set_timeout(self, value):
        self.timeout = value
        return self.timeout

    def set_max_time_wait(self, value):
        self.max_time_wait = value
        return self.max_time_wait

    def set_wait_time(self, value):
        self.wait_time = value
        return self.wait_time

    def get_timeout(self):
        return self.timeout
