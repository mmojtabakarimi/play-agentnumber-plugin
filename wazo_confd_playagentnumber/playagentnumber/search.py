from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from .model import PlayagentnumberModel

playagentnumber_config = SearchConfig(
    table=PlayagentnumberModel,
    columns={
        'id': PlayagentnumberModel.id,
        'exten': PlayagentnumberModel.exten,
        'blocked_num': PlayagentnumberModel.blocked_num,
    },
    default_sort='id',
)

playagentnumber_search = SearchSystem(playagentnumber_config)
