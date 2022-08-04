import logging

from flask import url_for, request, make_response
from flask_restful import Resource
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource, ListResource

from .model import PlayagentnumberModel
from .schema import PlayagentnumberSchema

logger = logging.getLogger(__name__)


class PlayagentnumberListResource(ListResource):
    schema = PlayagentnumberSchema
    model = PlayagentnumberModel

    def build_headers(self, model):
        return {'Location': url_for('playagentnumbers', uuid=model.id, _external=True)}

    @required_acl('confd.playagentnumbers.create')
    def post(self):
        return super().post()

    @required_acl('confd.playagentnumbers.read')
    def get(self):
        return super().get()


class PlayagentnumberItemResource(ItemResource):
    schema = PlayagentnumberSchema
    model = PlayagentnumberModel

    @required_acl('confd.playagentnumbers.read')
    def get(self, uuid):
        return super().get(uuid)

    @required_acl('confd.playagentnumbers.update')
    def put(self, uuid):
        return super().put(uuid)

    @required_acl('confd.playagentnumbers.delete')
    def delete(self, uuid):
        return super().delete(uuid)


class PlayagentnumberInquiryResource(Resource):
    def __init__(self, service):
        """
        :type service:PlayagentnumberService
        """
        self._service = service

    def get(self):
        tenant_uuid = request.headers.get('Wazo-Tenant')
        from_num = request.args.get('from_num')
        to_num = request.args.get('to_num')
        is_block = self._service.is_blocked_num(tenant_uuid, to_num, from_num)
        logger.info(f"Playagentnumber Inquiry {tenant_uuid} : {from_num} => {to_num} : {is_block}")

        response = "BLOCKED" if is_block else "NOT_BLOCKED"
        return make_response(response)
