import logging

from .playagentnumber.resource import PlayagentnumberInquiryResource, PlayagentnumberListResource, PlayagentnumberItemResource
from .playagentnumber.services import build_playagentnumber_service
from .db import init_db

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info('Playagentnumber plugin loading')
        init_db('postgresql://asterisk:proformatique@localhost/asterisk?application_name=wazo-playagentnumber-plugin')
        api = dependencies['api']
        playagentnumber_service = build_playagentnumber_service()

        # Playagentnumbers
        api.add_resource(
            PlayagentnumberListResource,
            '/playagentnumbers',
            resource_class_args=(playagentnumber_service,)
        )
        api.add_resource(
            PlayagentnumberItemResource,
            '/playagentnumbers/<int:uuid>',
            endpoint='playagentnumbers',
            resource_class_args=(playagentnumber_service,)
        )
        api.add_resource(
            PlayagentnumberInquiryResource,
            '/playagentnumbers/inquiry',
            resource_class_args=(playagentnumber_service,)
        )

        logger.info('Playagentnumber plugin loaded')
