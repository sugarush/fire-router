from unittest import skip

from sugar_asynctest import AsyncTestCase

from sugar_router import route, emit, methods


class TestRouter(AsyncTestCase):

    default_loop = True

    def test_get_methods(self):
        self.assertEqual(methods(), [ 'create', 'read', 'update', 'delete' ])

    def test_set_methods(self):
        methods([ 'get', 'post', 'put', 'delete' ])
        self.assertEqual(methods(), [ 'get', 'post', 'put', 'delete' ])

    async def test_emit_with_custom_method(self):

        methods([ 'get' ])

        @route('get', '/users')
        async def test():
            pass

        await emit('get', '/users')

        methods([ 'create', 'read', 'update', 'delete' ])

    async def test_emit_with_keywords(self):

        @route('create', '/users')
        async def test(value):
            self.assertEqual(value, 'value')

        await emit('create', '/users', value='value')

    async def test_route_with_argument(self):

        @route('create', '/users/:id')
        async def test(id):
            self.assertEqual(id, 'value')

        await emit('create', '/users/value')

    async def test_route_with_multiple_arguments(self):

        @route('create', '/users/:id/test/:name')
        async def test(id, name):
            self.assertEqual(id, 'value')
            self.assertEqual(name, 'value')

        await emit('create', '/users/value/test/value')
