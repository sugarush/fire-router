import re

__routes__ = { }
__methods__ = [ 'create', 'read', 'update', 'delete' ]


def methods(methods=None):
    global __methods__
    if methods:
        __methods__ = list(methods)
    else:
        return __methods__

def _check_method(method):
    if not method in __methods__:
        raise Exception(f'Method error: {method} not in {__methods__}')

def _get_paths(routes, method):
    _check_method(method)
    if not routes.get(method):
        routes[method] = { }
    return routes[method]

def _compile(path):
    return re.compile(re.sub('\:[^\/]*', '([^\/]*)', path))

def _match(paths, path):
    for (regex, handler) in paths.items():
        match = regex.fullmatch(path)
        if match:
            return (handler, match.groups())
    return None

def route(method, path):
    def wrapper(handler):
        global __routes__
        paths = _get_paths(__routes__, method)
        paths[_compile(path)] = handler
    return wrapper

async def emit(method, path, **kargs):
    _check_method(method)
    paths = __routes__.get(method)
    if not paths:
        return None
    handler, groups = _match(paths, path)
    if not handler:
        return None
    return await handler(*groups, **kargs)
