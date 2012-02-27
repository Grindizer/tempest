from tempest.common import rest_client
import json


class ExtensionsClient(object):

    def __init__(self, config, username, key, auth_url, tenant_name=None):
        self.config = config
        catalog_type = self.config.nova.catalog_type
        self.client = rest_client.RestClient(config, username, key,
                                             auth_url, catalog_type,
                                             tenant_name)

    def list_extensions(self):
        url = 'extensions'
        resp, body = self.client.get(url)
        body = json.loads(body)
        return resp, body
