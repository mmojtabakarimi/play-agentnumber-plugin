from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from .model import PlayagentnumbertModel

playagentnumber_config = SearchConfig(
    table=PlayagentnumbertModel,
    columns={
        'id': PlayagentnumbertModel.id,
        'exten': PlayagentnumbertModel.exten,
        'blocked_num': PlayagentnumbertModel.blocked_num,
    },
    default_sort='id',
)

playagentnumber_search = SearchSystem(playagentnumber_config)
