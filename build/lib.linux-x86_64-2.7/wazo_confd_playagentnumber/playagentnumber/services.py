from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_playagentnumber_notifier
from .validator import build_playagentnumber_validator


class PlayagentnumberService(CRUDService):
    def is_blocked_num(self, tenant_uuid, exten, blocked_num):
        """
        :rtype: bool
        """
        return self.dao.is_blocked_num(tenant_uuid, exten, blocked_num)


def build_playagentnumber_service():
    return PlayagentnumberService(dao, build_playagentnumber_validator(), build_playagentnumber_notifier())
