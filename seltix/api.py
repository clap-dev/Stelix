import requests

from .endpoints import API_PATH, API_DATA, ROOT

class InvalidMethod(Exception):
    '''Invalid method was passed.'''

class RequestHandler:
    '''Handles all requests sent to the Sellix API'''

    def get(**kwargs):
        return requests.get(
            API_PATH[kwargs['endpoint']] + '/{}'.format(kwargs['uniqid']),
            headers=kwargs['authorization']
        ).json()

    def list(**kwargs):
        return requests.get(
            API_PATH[kwargs['endpoint']] + '?page={page}'.format(page=kwargs['page']) if 'page' in kwargs else API_PATH[kwargs['endpoint']],
            headers=kwargs['authorization']
        ).json()

    def post(**kwargs):
        API, DATA = API_PATH[kwargs['endpoint']] + '/{}'.format(kwargs['uniqid']) if 'uniqid' in kwargs else API_PATH[kwargs['endpoint']], API_DATA[kwargs['endpoint']] if kwargs['endpoint'] in API_DATA else None

        if DATA:
            for key, value in DATA.items():
                if value:
                    DATA[key] = kwargs[key]

                else:
                    if key in kwargs:
                        DATA[key] = kwargs[key]

                    else:
                        DATA[key] = None

        return requests.post(
            API,
            json=DATA,
            headers=kwargs['authorization']
        ).json()

    def edit(**kwargs):
        API, DATA = API_PATH[kwargs['endpoint']] + '/{}'.format(kwargs['uniqid']), API_DATA[kwargs['endpoint']]

        for key, value in DATA.items():
            if key in kwargs:
                DATA[key] = kwargs[key]

            else:
                DATA[key] = None

        return requests.put(
            API,
            json=DATA,
            headers=kwargs['authorization']
        ).json()

    def delete(**kwargs):
        API = API_PATH[kwargs['endpoint']] + '/{}'.format(kwargs['uniqid'])

        return requests.delete(
            API,
            headers=kwargs['authorization']
        ).json()

class Sellix:
    '''The main class that the user will interact with'''

    def __init__(self, secret_key):
        self.secret_key = secret_key

        self.authorization = {
            'Authorization': 'Bearer {secret_key}'.format(secret_key=secret_key)
        }
        self.handles = {
            'get': RequestHandler.get,
            'list': RequestHandler.list,
            'edit': RequestHandler.edit,
            'post': RequestHandler.post,
            'create': RequestHandler.post,
            'delete': RequestHandler.delete,
        }

    def check(self, method, endpoint, **kwrags):
        API = self.handles.get(method, 'InvalidMethod')
        DATA = API_DATA.get(endpoint)

        if not callable(API):
            raise KeyError('Method does not exist.')

        if DATA:
            for key, value in DATA.items():
                if value:
                    if key not in kwrags:
                        raise KeyError('Missing required element {} inside the request data for {}'.format(key, endpoint))

    def request(self, method, endpoint, **kwargs):
        self.check(method, endpoint, **kwargs)

        kwargs['endpoint'] = endpoint
        kwargs['authorization'] = self.authorization

        return self.handles[method](**kwargs)
