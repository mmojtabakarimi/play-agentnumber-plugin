import logging

from .playagentnumber.resource import PlayagentnumberInquiryResource, PlayagentnumberListResource, PlayagentnumberItemResource
from .playagentnumber.services import build_blacklist_service
from .db import init_db

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info('Playagentnumber plugin loading')
        init_db('postgresql://asterisk:proformatique@localhost/asterisk?application_name=wazo-playagentnumber-plugin')
        api = dependencies['api']
        blacklist_service = build_blacklist_service()

        # Playagentnumbers
        api.add_resource(
            PlayagentnumberListResource,
            '/blacklists',
            resource_class_args=(blacklist_service,)
        )
        api.add_resource(
            PlayagentnumberItemResource,
            '/blacklists/<int:uuid>',
            endpoint='blacklists',
            resource_class_args=(blacklist_service,)
        )
        api.add_resource(
            PlayagentnumberInquiryResource,
            '/blacklists/inquiry',
            resource_class_args=(blacklist_service,)
        )

        logger.info('Playagentnumber plugin loaded')
