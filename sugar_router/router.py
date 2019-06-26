import re


def _compile(path):
    return re.compile(re.sub('\:[^\/]*', '([^\/]*)', path))


class Router(object):

    def __init__(self, methods=[ 'get', 'head', 'post', 'put', 'delete', 'connect', 'options', 'trace', 'patch' ]):
        self.__routes__ = { }
        self.__methods__ = methods

    def __getattribute__(self, name):
        if name in super(Router, self).__getattribute__('__methods__'):
            return lambda path: self.route(name, path)
        else:
            return super(Router, self).__getattribute__(name)

    def _check_method(self, method):
        if not method in self.__methods__:
            raise Exception(f'Method error: {method} not in {self.__methods__}')

    def _get_paths(self, method):
        self._check_method(method)
        if not self.__routes__.get(method):
            self.__routes__[method] = { }
        return self.__routes__[method]

    def _match(self, method, path):
        self._check_method(method)
        paths = self.__routes__.get(method)
        if not paths:
            return None
        for (regex, handler) in paths.items():
            match = regex.fullmatch(path)
            if match:
                return (handler, match.groups())
        return None

    def route(self, method, path):
        def wrapper(handler):
            paths = self._get_paths(method)
            paths[_compile(path)] = handler
        return wrapper

    async def emit(self, method, path, **kargs):
        handler, groups = self._match(method, path)
        if not handler:
            return None
        return await handler(*groups, **kargs)
