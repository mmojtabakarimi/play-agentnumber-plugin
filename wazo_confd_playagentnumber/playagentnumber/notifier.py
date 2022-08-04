from wazo_confd import bus, sysconfd


class BlacklistNotifier:
    def __init__(self, bus, sysconfd):
        self.bus = bus
        self.sysconfd = sysconfd

    def send_sysconfd_handlers(self):
        pass

    def created(self, blacklist):
        pass

    def edited(self, blacklist):
        pass

    def deleted(self, blacklist):
        pass


def build_blacklist_notifier():
    return BlacklistNotifier(bus, sysconfd)
