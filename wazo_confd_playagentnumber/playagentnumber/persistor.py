from xivo_dao.helpers.persistor import BasePersistor
from xivo_dao.resources.utils.search import CriteriaBuilderMixin

from .model import PlayagentnumberModel


class PlayagentnumberPersistor(CriteriaBuilderMixin, BasePersistor):
    _search_table = PlayagentnumberModel

    def __init__(self, session, playagentnumber_search, tenant_uuids=None):
        self.session = session
        self.search_system = playagentnumber_search
        self.tenant_uuids = tenant_uuids

    def _find_query(self, criteria):
        query = self.session.query(PlayagentnumberModel)
        # query = self._filter_tenant_uuid(query)
        return self.build_criteria(query, criteria)

    def _search_query(self):
        return self.session.query(self.search_system.config.table)

    def is_blocked_num(self, tenant_uuid, exten, blocked_num):
        """
        :type tenant_uuid: str
        :type exten: str
        :type blocked_num: str
        :return: is blocked
        :rtype: bool
        """
        blocked_by_tenant = self.session.query(PlayagentnumberModel) \
            .filter(PlayagentnumberModel.exten.is_(None), PlayagentnumberModel.blocked_num == blocked_num)

        if tenant_uuid:
            blocked_by_tenant = blocked_by_tenant.filter(PlayagentnumberModel.tenant_uuid == tenant_uuid)

        if blocked_by_tenant.count():
            return True

        if not exten:
            return False

        blocked_by_exten = self.session.query(PlayagentnumberModel) \
            .filter(PlayagentnumberModel.exten == exten, PlayagentnumberModel.blocked_num == blocked_num)

        if tenant_uuid:
            blocked_by_exten = blocked_by_exten.filter(PlayagentnumberModel.tenant_uuid == tenant_uuid)

        return blocked_by_exten.count() > 0
