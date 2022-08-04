from xivo_dao.helpers.db_manager import daosession

from .persistor import PlayagentnumberPersistor
from .search import playagentnumber_search


@daosession
def _persistor(session, tenant_uuids=None):
    return PlayagentnumberPersistor(session, Playagentnumber_search, tenant_uuids)


def search(tenant_uuids=None, **parameters):
    return _persistor(tenant_uuids).search(parameters)


def get(Playagentnumber_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).get_by({'id': Playagentnumber_uuid})


def get_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).get_by(criteria)


def find(Playagentnumber_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).find_by({'id': Playagentnumber_uuid})


def find_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_by(criteria)


def find_all_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_all_by(criteria)


def create(Playagentnumber):
    return _persistor().create(Playagentnumber)


def edit(Playagentnumber):
    _persistor().edit(Playagentnumber)


def delete(Playagentnumber):
    _persistor().delete(Playagentnumber)


def is_blocked_num(tenant_uuid, exten, blocked_num):
    return _persistor().is_blocked_num(tenant_uuid, exten, blocked_num)
