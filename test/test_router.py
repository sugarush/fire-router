from sugar_asynctest import AsyncTestCase

from sugar_router import Router


class TestRouter(AsyncTestCase):

    default_loop = True

    async def test_emit_with_custom_method(self):

        router = Router()

        @router.route('get', '/users')
        async def test():
            return 'value'

        result = await router.emit('get', '/users')

        self.assertEqual(result, 'value')

    async def test_emit_with_keyword(self):

        router = Router()

        @router.get('/users')
        async def test(value):
            self.assertEqual(value, 'value')

        await router.emit('get', '/users', value='value')

    async def test_route_with_dynamic_method(self):

        router = Router()

        @router.get('/users')
        async def test():
            return 'value'

        result = await router.emit('get', '/users')

        self.assertEqual(result, 'value')

    async def test_route_with_argument(self):

        router = Router()

        @router.get('/users/:id')
        async def test(id):
            self.assertEqual(id, 'value')

        await router.emit('get', '/users/value')

    async def test_route_with_multiple_arguments(self):

        router = Router()

        @router.get('/users/:id/test/:name')
        async def test(id, name):
            self.assertEqual(id, 'value')
            self.assertEqual(name, 'value')

        await router.emit('get', '/users/value/test/value')
