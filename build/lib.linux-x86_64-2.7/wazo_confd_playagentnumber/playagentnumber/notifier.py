from wazo_confd import bus, sysconfd


class PlayagentnumberNotifier:
    def __init__(self, bus, sysconfd):
        self.bus = bus
        self.sysconfd = sysconfd

    def send_sysconfd_handlers(self):
        pass

    def created(self, playagentnumber):
        pass

    def edited(self, playagentnumber):
        pass

    def deleted(self, playagentnumber):
        pass


def build_playagentnumber_notifier():
    return PlayagentnumberNotifier(bus, sysconfd)
